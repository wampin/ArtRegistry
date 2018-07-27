CREATE TABLE piece
(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	title VARCHAR(100) NOT NULL,
	medium VARCHAR(100), 
	dimensions DOUBLE,
	signature_location VARCHAR(40),
	date_completed TEXT NOT NULL,
	notes
);

CREATE TABLE sold
( 
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	gallery_id INTEGER NOT NULL,
	contacts_id INTEGER NOT NULL,
	wholesale INTEGER NOT NULL,
	gallery_percent INTEGER NOT NULL,
	date_purchased TEXT INTEGER NOT NULL,
	FOREIGN KEY(gallery_id) REFERENCES gallery(id),
	FOREIGN KEY(contacts_id) REFERENCES contacts(id)
);

CREATE TABLE contact
(
	id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	address VARCHAR(150),
	city VARCHAR(50),
	state NCHAR(2),
	zip NCHAR(5),
	phone INTEGER,
	gallery_id INTEGER,
	FOREIGN KEY(gallery_id) REFERENCES gallery(id)
);

CREATE TABLE gallery
(
	id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	name VARCHAR(50) NOT NULL,
	address VARCHAR(150),
	city VARCHAR(50),
	state NCHAR(2),
	zip NCHAR(5),
	phone INTEGER
);

CREATE TABLE show
(
	id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	gallery_id INTEGER NOT NULL,
	date_start TEXT NOT NULL,
	date_end TEXT NOT NULL,
	FOREIGN KEY(gallery_id) REFERENCES gallery(id)
);

CREATE TABLE show_piece
(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	show_id INTEGER NOT NULL,
	piece_id INTEGER NOT NULL,
	FOREIGN KEY(piece_id) REFERENCES piece(id)
	FOREIGN KEY(show_id) REFERENCES piece(id)
);

