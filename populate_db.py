from app import db
from models import Book, Genre
import csv
import sys
from flask import Flask

## run only one time
def populate():
	filename = 'book30-listing-test-condense.csv'
	genres = dict()
	book_obj_list = []
	with open(filename) as f:
		reader = csv.reader(f, delimiter=',')
		for row in reader:
			image_url = row[0]
			title = row[1]
			author = row[2]
			genre = row[3]
			genre_to_save = ''
			genre_obj = None
			## print(f"image_url: '{image_url}' title: '{title}' author: '{author}' genre: '{genre}'")

			## append genres if not in genres
			if (genres.get(genre) == None):
				genre_obj = Genre(name = genre)	
				genres[genre] = 1
				db.session.add(genre_obj)
				db.session.commit()
			else:
				genre_obj = Genre.query.filter_by(name = genre).first()


			book = Book(image_url = image_url, title = title, author = author, genre = genre_obj)
			book_obj_list.append(book)

	db.session.add_all(book_obj_list)
	db.session.commit()