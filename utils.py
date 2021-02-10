from flask import current_app, request, jsonify
from models import User
from functools import wraps
import jwt
import sys

## define a decorator that requires a valid JWT token in order to successfully respond to a request 
def token_required(f):
	@wraps(f)
	def _verify(*args, **kwargs):
		auth_headers = request.headers.get('Authorization', '').split()

		invalid_msg = {
			'message' : 'Invalid token. Registration and/or authentication required',
			'authenticated' : False	
		}

		expired_msg = {
			'message' : 'Expired token. Reauthentication required.',
			'authenticated' : False	
		}

		if (len(auth_headers) != 2):
			return jsonify(invalid_msg), 401
		try:

			## try to find the user for the email that is given through the JWT 
			token = auth_headers[1]
			print(token, file = sys.stderr)
			data = jwt.decode(token, current_app.config['SECRET_KEY'])
			print(data, file = sys.stderr)
			user = User.query.filter_by(email = data['sub']).first()
			if (not user):
				raise RuntimeError('User not found')
			return f(user, *args, **kwargs)

		except jwt.ExpiredSignatureError:
			return jsonify(expired_msg), 401
		except jwt.InvalidTokenError:
			return jsonify(invalid_msg), 401
		except Exception as e:
			print('error: ', str(e), file = sys.stderr)
			return jsonify({'error' : 'error'}), 500


	return _verify
