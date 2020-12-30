from flask import Flask, jsonify, request, Blueprint, current_app
from flask_cors import CORS  
from models import User, Book, Genre, Library, LibraryBook, UserBook
from app import db
from datetime import datetime, timedelta
from functools import wraps
from utils import token_required
import math
from random import randint
import jwt
import uuid
import csv
import sys 
api = Blueprint('api', __name__)
CORS(api, resources={r'/*': {'origins' : '*'}})

BOOKS = [
    {
    	'id' : uuid.uuid4().hex,
        'title': 'On the Road',
        'author': 'Jack Kerouac',
        'read': True
    },
    {
    	'id' : uuid.uuid4().hex,
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'author': 'J. K. Rowling',
        'read': False
    },
    {
    	'id' : uuid.uuid4().hex,
        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
        'read': True
    }
]

# sanity check route
@api.route('/ping', methods = ['GET'])
def ping_pong():
	return jsonify('pong!')

@api.route('/test', methods = ['GET'])
@token_required
def test():
	return jsonify('logged in!')

@api.route('/register', methods = ['POST'])
def register():
	data = request.get_json()
	## make sure a user with the requested email does not exist 
	user = User.query.filter_by(email=data.get('email')).first()
	if (not user):
		## hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')

		## generate an 8 digit number represented as a string (leading zeroes are valid here)
		card_num_length = 8 
		library_card_num = ''.join(["{}".format(randint(0, 9)) for num in range(0, card_num_length)])
		user = User(firstname = data.get('firstname'), 
			lastname = data.get('lastname'), 
			email=data.get('email'), 
			password=data.get('password'), 
			library_card_num = library_card_num)
		db.session.add(user)
		db.session.commit()
		return jsonify({'message' : 'User created successfully!'}), 200
	else:
		return jsonify({'message' : 'Email has already been taken!'}), 500 

@api.route('/login', methods = ['POST'])
def login():
	data = request.get_json()
	user = User.query.filter_by(email=data.get('email')).first()
	if (user and user.password == data.get('password')):
		token = jwt.encode({
			'sub' : user.email,
			'iat' : datetime.utcnow(),
			'exp' : datetime.utcnow() + timedelta(minutes = 30)
		}, current_app.config['SECRET_KEY'])	
		return jsonify({'token' : token.decode('UTF-8'), 'message' : 'Login Success!', 'authenticated' : True}), 200
	else:
		return jsonify({'message' : 'Invalid credentials', 'authenticated' : False}), 401

	# if user and bcrypt.check_password_hash(user.password, form.password.data):
	# 	login_user(user, remember=form.remember.data)
	# 	## if the user accesses a protected route, redirect them to their intended page after login based
	# 	## on the route listed in the query parameter 
	# 	flash(f'You have been logged in!', 'success')
	# 	next_page = request.args.get('next')
	# 	if (not is_safe_url(next_page)):
	# 		return abort(400)
	# 	return redirect(next_page or url_for('main.home'))
	# else:
	# 	flash(f'Login Unsuccessful, Please check email and password', 'danger')

@api.route('/logout', methods = ['POST'])
def logout():
	## do not return a token
	return jsonify({'message' : 'Logout Success!'}), 200

@api.route('/libraries', methods = ['GET'])
def libraries():
	libraries = Library.query.all()
	return jsonify({'message' : 'Libraries found successfully!', 'data' : [l.to_dict() for l in libraries]}), 200

@api.route('/genres', methods = ['GET'])
def genres():
	genres = Genre.query.all()
	return jsonify({'message' : 'Genres found successfully!', 'data' : [g.to_dict() for g in genres]}), 200

@api.route('/search', methods = ['GET'])
def catalog_search():
	data = []
	if (request.method == 'GET'):
		library_books = LibraryBook.query
		print(request.args, file = sys.stderr)
		if (int(request.args.get('library_id')) != 0):
			library_books = library_books.filter_by(library_id = request.args.get('library_id'))
		if (request.args.get('title') != '' or int(request.args.get('genre_id')) != 0):
			library_books = LibraryBook.query.join(LibraryBook.book, aliased=True)
			if (request.args.get('title') != ''):
				library_books = library_books.filter(Book.title.like('%' + request.args.get('title') + '%'))
			if (int(request.args.get('genre_id')) != 0):
				library_books = library_books.filter_by(genre_id = request.args.get('genre_id'))
		print(library_books, file = sys.stderr)

		library_books = library_books.all()
		data = generate_book_result_arr(library_books)

	return jsonify({'message' : 'Search Successful!', 'data': data}), 200

@api.route('/books', methods = ['GET', 'POST'])
def all_books():
	response_object = {'status' : 'success'}
	if (request.method == 'POST'):
		pass
	else:

		library_books = LibraryBook.query.all()
		response_object['data'] = generate_book_result_arr(library_books) 

	return jsonify(response_object)

@api.route('/books/<book_id>', methods=['PUT', 'DELETE'])
def single_book(book_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_book(book_id)
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Book updated!'

    if (request.method == "DELETE"):
    	remove_book(book_id)
    	response_object['message'] = 'Book removed!'

    return jsonify(response_object)

def remove_book(book_id):
    for book in BOOKS:
        if book['id'] == book_id:
            BOOKS.remove(book)
            return True
    return False

## take in library book flask sql alchemy query object and return dictionary with proper format including the books
## and the library mapped to 
def generate_book_result_arr(library_books):
	book_obj = dict() 
	for library_book in library_books:
		if (book_obj.get(library_book.book_id) != None):
			book_obj[library_book.book_id]['library'][library_book.library.name] = library_book.book_status.name	
			book_obj[library_book.book_id]['library_book_ids'][library_book.library.name] = library_book.id	
				
		else:	
			to_insert = {
				'library' : {
					library_book.library.name : library_book.book_status.name
				},
				'library_book_ids' : {
					library_book.library.name : library_book.id
				}
			}
			book_dict = library_book.book.to_dict()
			for key in book_dict:
				to_insert[key] = book_dict[key]
			book_obj[library_book.book_id] = to_insert 

	book_arr = [book_obj[book_id] for book_id in book_obj]
	return book_arr

