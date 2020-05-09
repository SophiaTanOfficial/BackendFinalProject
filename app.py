import json
from flask import Flask, request
import dao
from db import db

app = Flask(__name__)
db_filename = "FinalProject.db"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///%s" % db_filename
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

db.init_app(app)
with app.app_context():
    db.create_all()

# generalized response formats
def success_response(data, code=200):
    return json.dumps({"success": True, "data": data}), code

def failure_response(message, code=404):
    return json.dumps({"success": False, "error": message}), code
# your routes here
#-- BOOK ROUTES ------------------------------------------------------

@app.route('/')
@app.route('/api/books/')
def get_books():
    return success_response(dao.get_all_books())

@app.route('/api/books/', methods = ['POST'])
def create_book():
    body = json.loads(request.data)
    book = dao.create_book(
        title = body.get('title'),
        author = body.get('author')
    )
    return success_response(book, 201)

@app.route('/api/books/<int:book_id>/')
def get_book(book_id):
    book = dao.get_book_by_id(book_id)
    if book is None:
        return failure_response("Book not found!")
    return success_response(book)

@app.route('/api/books/<int:book_id>/', methods = ['DELETE'])
def delete_book(book_id):
    book = dao.delete_book_by_id(book_id)
    if book is None:
        return failure_response("Book not found!")
    return success_response(book)

# @app.route('/api/books/<int:book_id>/like/', methods = ['POST'])
# def like_book(book_id):
#     body = json.loads(request.data)
#
#     book = dao.like_a_book(
#         book_id
#     )
#     if book is None:
#         return failure_response("Book/User not found! Please check your entered IDs.")
#     # return success_response(task)
#     return success_response(book)
#
# @app.route('/api/books/<int:book_id>/dislike/', methods = ['POST'])
# def dislike_book(book_id):
#     body = json.loads(request.data)
#
#     book = dao.dislike_a_book(
#         book_id
#     )
#     if book is None:
#         return failure_response("Book/User not found! Please check your entered IDs.")
#     # return success_response(task)
#     return success_response(book)

#-- USER ROUTES ------------------------------------------------------
@app.route('/api/users/')
def get_users():
    return success_response(dao.get_all_users())

@app.route('/api/users/', methods = ['POST'])
def create_user():
    body = json.loads(request.data)
    user = dao.create_user(
        body.get('name'),
        body.get('username'),
        body.get('favorite_book')
    )
    return success_response(user)

@app.route('/api/users/<int:user_id>/')
def get_user(user_id):
    user = dao.get_user_by_id(user_id)
    if user is None:
        return failure_response("User not found!")
    return success_response(user)

@app.route('/api/books/<int:book_id>/add/', methods = ['POST'])
def add_user(book_id):
    body = json.loads(request.data)

    book = dao.assign_user(
        book_id,
        body.get('user_id'),
    )
    if book is None:
        return failure_response("Book/User not found! Please check your entered IDs.")
    # return success_response(task)
    return success_response(book)

@app.route('/api/users/<int:user_id>/', methods = ['POST'])
def update_fav_book(user_id):
    body = json.loads(request.data)

    user = dao.update_fav_book(
        user_id,
        body
    )
    if user is None:
        return failure_response("User not found!")
    return success_response(user)

@app.route('/api/users/<int:user_id>/delete_recommended/', methods = ['POST'])
def delete_recommended_book(user_id):
    body = json.loads(request.data)

    user = dao.delete_recommended_book(
        user_id,
        body
    )
    if user is None:
        return failure_response("User/Book not found! Please check your IDs.")
    return success_response(user)

@app.route('/api/users/<int:user_id>/add_read/', methods = ['POST'])
def add_to_read(user_id):
    body = json.loads(request.data)

    book = dao.add_to_read(
        user_id,
        body.get("book_id")
    )
    if book is None:
        return failure_response("Book/User not found! Please check your entered IDs.")
    # return success_response(task)
    return success_response(book)


#-- REVIEW ROUTES ------------------------------------------------------
@app.route('/api/books/<int:book_id>/review/', methods=['POST'])
def create_review(book_id):
    book = dao.get_book_by_id(book_id)
    if book is None:
        return failure_response("Book not found!")
    body = json.loads(request.data)
    review = dao.create_review(
        body.get('username'),
        body.get('review'),
        body.get('recommend'),
        book_id
    )
    return success_response(review)

@app.route('/api/reviews/<int:review_id>/update/', methods=['POST'])
def update_review(review_id):
    review = dao.get_review(review_id)
    body = json.loads(request.data)
    if review is None:
        return failure_response("Review not found!")
    review = dao.update_review(
        review_id,
        body
    )
    return success_response(review)

@app.route('/api/reviews/<int:review_id>/', methods = ['DELETE'])
def delete_review(review_id):
    review = dao.delete_review(review_id)
    if review is None:
        return failure_response("Review not found!")
    return success_response(review)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
