from flask import Flask, jsonify, request, Blueprint, current_app
from flask_cors import CORS  
from models import User
from datetime import datetime, timedelta
from functools import wraps
from utils import token_required
import math
import jwt
import uuid
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
		library_card_num = ''.join(["{}".format(randint(0, 9)) for num in range(0, n)])
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

@api.route('/books', methods = ['GET', 'POST'])
def all_books():
	response_object = {'status' : 'success'}
	if (request.method == 'POST'):
		post_data = request.get_json()
		BOOKS.append({
			'id' : uuid.uuid4().hex,
			'title' : post_data.get('title'),
			'author' : post_data.get('author'),
			'read' : post_data.get('read')
		})
		response_object['message'] = 'Book added!'
	else:
		response_object['books'] = BOOKS

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

