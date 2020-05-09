from db import db, User, Book, Review

# your methods here
#-----BOOK------------------------------
def get_all_books():
    return[t.serialize() for t in Book.query.all()]

def create_book(title, author):
    new_book = Book(
    title = title,
    author = author,
    likes = 0,
    dislikes = 0
    )

    db.session.add(new_book) #Having add and commit on separate lines allows us to add
    #several objects before committing, better runtime
    db.session.commit()
    return new_book.serialize()

def get_book_by_id(book_id):
    book = Book.query.filter_by(id = book_id).first()
    if book is None:
        return None
    return book.serialize()

def delete_book_by_id(book_id):
    book = Book.query.filter_by(id = book_id).first()
    if book is None:
        return None
    db.session.delete(book)
    db.session.commit()
    return book.serialize()

# def like_a_book(book_id):
#     book = Book.query.filter_by(id = book_id).first()
#     if book is None:
#         return None
#     book.likes += 1
#     db.session.commit()
#     return book.serialize()
#
# def dislike_a_book(book_id):
#     book = Book.query.filter_by(id = book_id).first()
#     if book is None:
#         return None
#     book.dislikes += 1
#     db.session.commit()
#     return book.serialize()
#-----USERS----------------------------------
def get_all_users():
    return[t.serialize() for t in User.query.all()]

def create_user(name, username, favorite_book):
    new_user = User(
        name = name,
        username = username,
        favorite_book = favorite_book
    )

    db.session.add(new_user)
    db.session.commit()
    return new_user.serialize()

def get_user_by_id(user_id):
    user = User.query.filter_by(id = user_id).first()
    if user is None:
        return None
    return user.serialize()

def assign_user(book_id, user_id):
    book = Book.query.filter_by(id = book_id).first()
    if book is None:
        return None
    user = User.query.filter_by(id = user_id).first()
    if user is None:
        return None
    book.recommending_users.append(user)
    user.recommended_books.append(book)
    db.session.commit()
    return user.serialize() #Only shows book added to user

def add_to_read(user_id, book_id):
    book = Book.query.filter_by(id = book_id).first()
    if book is None:
        return None

    user = User.query.filter_by(id = user_id).first()
    if user is None:
        return None
    book.users_who_read.append(user)
    user.read.append(book)
    db.session.commit()
    return user.serialize() #Only shows book added to user

def update_fav_book(user_id, body):
    user = User.query.filter_by(id = user_id).first()
    if user is None:
        return None

    user.favorite_book = body.get("favorite_book", user.favorite_book)
    #Place current value of favbook as default if no new value provided

    db.session.commit()
    return user.serialize()

def delete_recommended_book(user_id, body):
    user = User.query.filter_by(id= user_id).first()
    book_id = body.get("book_id")
    if user is None:
        return None
    recommended_books = user.recommended_books
    book = None
    pos = 0
    finalpos = 0
    #loop through recommended books to see if book is in list
    for x in recommended_books:
        if x.id == book_id:
            book = x
            finalpos = pos
        pos += 1

    if book is None:
        return None

    user.recommended_books.pop(finalpos) #Delete the book from recommended list
    db.session.commit()
    return user.serialize()



#-----REVIEW-------------------------------
def create_review(username, review, recommend, book_id):
    # if recommend == True:
    #     recommendation = "Yes"
    # else:
    #     recommendation = "No"

    new_review = Review(
        username = username,
        review = review,
        recommend = recommend,
        book = book_id

    )

    db.session.add(new_review)
    db.session.commit()
    return new_review.serialize()

def get_review(review_id):
    review = Review.query.filter_by(id = review_id).first()
    if review is None:
        return None
    return review.serialize()

def update_review(review_id, body):
    review = Review.query.filter_by(id = review_id).first()
    review.review = body.get("review", review.review)
    review.recommend = body.get('recommend', review.recommend)
    db.session.commit()
    return review.serialize()

def delete_review(review_id):
    review = Review.query.filter_by(id = review_id).first()
    if review is None:
        return None
    db.session.delete(review)
    db.session.commit()
    return review.serialize()

def query(book_id):
    book = Book.query.filter_by(id = book_id).first()
    return book
