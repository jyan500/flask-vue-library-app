from datetime import datetime 
from app import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	firstname = db.Column(db.String(120), nullable = False)
	lastname = db.Column(db.String(120), nullable = False)
	library_card_num = db.Column(db.String(255), nullable = False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	password = db.Column(db.String(255), nullable=False)
	user_books = db.relationship('UserBook', backref = 'user_book', lazy = True)

	def __repr__(self):
		return f"User('{self.username}', '{self.email}')"

	def to_dict():
		return dict(id = self.id, firstname = self.firstname, lastname = self.lastname, library_card_num = self.library_card_num, email = self.email)


class Genre(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(120), nullable = False)
	books = db.relationship('Book', backref = 'books', lazy = True)

	def __repr__(self):
		return f"Genre('{self.name}')"

	def to_dict(self):
		return dict(id = self.id, name = self.name)

class Book(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(255), nullable = False)
	image_url = db.Column(db.String(255), nullable = True)
	author = db.Column(db.String(255), nullable = True)
	genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'), nullable = False)
	genre = db.relationship('Genre', backref = 'genre', lazy = True)

	def __repr__(self):
		return f"Book('{self.title}', '{self.image_url}', '{self.author}')"

	def to_dict(self):
		return dict(id = self.id, title = self.title, image_url = self.image_url, author = self.author, genre = self.genre.to_dict())

class Library(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255), nullable = False)
	address = db.Column(db.String(255), nullable = True)
	city = db.Column(db.String(255), nullable = True)
	state = db.Column(db.String(255), nullable = True)
	zipcode = db.Column(db.String(255), nullable = True)
	image_url = db.Column(db.String(255), nullable = True)

	def __repr__(self):
		return f"Library('{self.name}', '{self.address}')"

	def to_dict(self):
		return dict(id = self.id, name = self.name, address = f"{self.address}, {self.city} {self.state} {self.zipcode}", image_url = self.image_url)

class LibraryBook(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable = False)
	library_id = db.Column(db.Integer, db.ForeignKey('library.id'), nullable = False)
	book_status_id = db.Column(db.Integer, db.ForeignKey('book_status.id'), nullable = False)
	book_status = db.relationship('BookStatus', backref = 'status', lazy = True)
	library = db.relationship('Library', backref = 'library', lazy = True)
	book = db.relationship('Book', backref = 'book', lazy = True)

	def __repr__(self):
		return f"LibraryBook('{self.book_id}', '{self.library_id}', '{self.book_status_id}')"

	def to_dict(self):
		return dict(id = self.id, book = self.book.to_dict(), library = self.library.to_dict(), book_status = self.book_status.to_dict())

class BookStatus(db.Model):
	## book can be checked out, on shelf, missing, overdue
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(255), nullable = False)

	def __repr__(self):
		return f"BookStatus('{self.name}')"

	def to_dict(self):
		return dict(id = self.id, name = self.name)

class UserBook(db.Model):
	## book that user has checked out from a library
	id = db.Column(db.Integer, primary_key = True)
	library_book_id = db.Column(db.Integer, db.ForeignKey('library_book.id'), nullable = False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
	date_borrowed = db.Column(db.DateTime, nullable = True)
	date_due = db.Column(db.DateTime, nullable = True)
	date_returned = db.Column(db.DateTime, nullable = True)
	user = db.relationship('User', backref = 'user', lazy = True)
	library_book = db.relationship('LibraryBook', backref = 'library_book', lazy = True)

	def __repr__(self):
		return f"UserBook"

	def to_dict():
		return dict(id = self.id, library_book = self.library_book.to_dict(), user = self.user.to_dict(), date_due = self.date_due, date_returned = self.date_returned, date_borrowed = self.date_borrowed)










