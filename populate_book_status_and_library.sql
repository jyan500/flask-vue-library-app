SELECT * FROM flask_vue_library.book_status;


insert into book_status set name = 'On Shelf';
insert into book_status set name = 'Borrowed';
insert into book_status set name = 'On Hold';
insert into book_status set name = 'Overdue';
insert into book_status set name = 'Missing';

insert into library set name = 'San Mateo Public Library', address = '55 W 3rd Ave', city = 'San Mateo', state = 'CA',
zipcode = '94402', image_url = 'https://www.cityofsanmateo.org/ImageRepository/Document?documentID=60693';

insert into library set name = 'Millbrae Public Library', address = '1 Library Ave', city = 'Millbrae', state = 'CA',
zipcode = '94030', image_url = 'https://smcl.bibliocommons.com/locations/uploads/images/full/5c5c9e417bbccebf12b0ed94930997b6/millbrae.jpg';

insert into library set name = 'South San Francisco Public Library', address = '306 Walnut Ave', state = 'CA', 
city = 'South San Francisco', zipcode = '94080', image_url = 'https://www.ssf.net/Home/ShowPublishedImage/557/636392609136430000';

insert into library_book (book_id, library_id, book_status_id) 
SELECT id, 1, 1 FROM book;

insert into library_book (book_id, library_id, book_status_id)
SELECT id, 2, 1 FROM book;

insert into library_book (book_id, library_id, book_status_id)
SELECT id, 3, 1 FROM book;