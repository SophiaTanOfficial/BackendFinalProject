from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#many to many relationship between users and books
association_table = db.Table('association', db.Model.metadata,
    db.Column('book_id', db.Integer, db.ForeignKey('book.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    )

read_association_table = db.Table('read_association', db.Model.metadata,
    db.Column('book_id', db.Integer, db.ForeignKey('book.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    )
class Book(db.Model): #In SQLAlchemy, we tell it that it's a table by saying Model
    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String, nullable = False)
    author = db.Column(db.String, nullable = False)
    reviews = db.relationship('Review', cascade = 'delete')
    users_who_read = db.relationship('User', secondary = read_association_table, back_populates = 'read')
    recommending_users = db.relationship('User', secondary = association_table, back_populates = 'recommended_books')


    def __init__(self, **kwargs):
        #Constructor takes in column info that we need, in this case, description and done
        self.title = kwargs.get('title', '')
        self.author = kwargs.get('author', '')


    def serialize_helper(self, input, type):
        if type == 'users':
            users = []
            for x in input:
                users.append({'id': x.id, 'username': x.username})
            return users
        if type == 'reviews':
            reviews = []
            for x in input:
                reviews.append({'id': x.id, 'username': x.username, 'review': x.review, 'recommend': x.recommend})
            return reviews
    #We need to be able to properly return our data to our clients in the form of Jsson
    def serialize(self):
        #interprets our column data per row as jsson format
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'reviews': self.serialize_helper(self.reviews, 'reviews'),
            'users_who_read': self.serialize_helper(self.users_who_read, 'users'),
            'recommending_users': self.serialize_helper(self.recommending_users, 'users')
        }


#User Table
class User(db.Model): #In SQLAlchemy, we tell it that it's a table by saying Model
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    username = db.Column(db.String, nullable = False)
    favorite_book = db.Column(db.String, nullable = True)
    read = db.relationship('Book', secondary = read_association_table, back_populates = 'users_who_read')
    recommended_books = db.relationship('Book', secondary = association_table, back_populates = 'recommending_users')



    #Create a constructor. For each new row we add to the table, it's essentially an object we have to initialize
    def __init__(self, **kwargs):
        #Constructor takes in column info that we need, in this case, description and done
        self.name = kwargs.get('name', '')
        self.username = kwargs.get('username', '')
        self.favorite_book = kwargs.get('favorite_book', 'None')


    def serialize_helper(self, input):
        books = []
        for x in input:
            books.append({'id': x.id, 'title': x.title})
        return books



    #We need to be able to properly return our data to our clients in the form of Jsson
    def serialize(self):
        #interprets our column data per row as jsson format
        return {
            'id': self.id,
            'name': self.name,
            'username': self.username,
            'favorite_book': self.favorite_book,
            'read': self.serialize_helper(self.read),
            'recommended_books': self.serialize_helper(self.recommended_books)
        }

class Review(db.Model):
    __tablename__ = 'review'
    id = db.Column(db.Integer, primary_key= True)
    username = db.Column(db.String, nullable = False)
    review = db.Column(db.String, nullable = False)
    recommend = db.Column(db.String, nullable = False)
    book = db.Column(db.Integer, db.ForeignKey('book.id'), nullable = False)

    def __init__(self, **kwargs): #kwargs is python syntax which means this method can take on any number of arguments
        self.username = kwargs.get('username', '')
        self.review = kwargs.get('review', '')
        self.recommend = kwargs.get('recommend', 'No')
        self.book = kwargs.get('book')

    def serialize_book_omit(self, x):
        return {'id': x.id, 'title': x.title, 'author': x.author}

    def serialize(self):
        return {
        'id': self.id,
        'username': self.username,
        'review': self.review,
        'recommend': self.recommend,
        'book': self.serialize_book_omit(Book.query.filter_by(id = self.book).first())
        }
