import sqlite3
import sys

dbPath = ":memory:"
conn = sqlite3.connect(dbPath)
c = conn.cursor()

def CreateTables():
    '''creates the tables for Art Register database'''

    # Create piece table
    c.execute('''
                CREATE TABLE piece
                (
                    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                    title VARCHAR(100) NOT NULL,
                    medium VARCHAR(100), 
                    dimensions VARCHAR(100),
                    signature_location VARCHAR(40),
                    date_completed VARCHAR(100) NOT NULL,
                    notes VARCHAR(100)
                );
            ''')

    # Create sold table
    # Columns: gallery_id, contacts_id, wholesale, gallery_percent, date_purchased, gallery(id),contacts(id)
    c.execute('''
                CREATE TABLE sold
                ( 
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        gallery_id INTEGER NOT NULL,
                        contacts_id INTEGER NOT NULL,
                        wholesale INTEGER NOT NULL,
                        gallery_percent INTEGER NOT NULL,
                        date_purchased VARCHAR(100) NOT NULL,
                        FOREIGN KEY(gallery_id) REFERENCES gallery(id),
                        FOREIGN KEY(contacts_id) REFERENCES contacts(id)
                );
            ''');

    # Create contact table
    # Columns: address, city, state, zip, phone, gallery_id
    c.execute('''
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
            ''');

    # Create gallery table
    # Columns: name, address, city, state, zip, phone
    c.execute('''
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
            ''');

    # Create show table
    # Columns: gallery_id, date_start, date_end 
    c.execute('''
                CREATE TABLE show
                (
                        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                    gallery_id INTEGER NOT NULL,
                    date_start VARCHAR(100) NOT NULL,
                    date_end VARCHAR(100) NOT NULL,
                    FOREIGN KEY(gallery_id) REFERENCES gallery(id)
            );
        ''');

    # Create show_piece table
    # Columns: show_id, piece_id
    c.execute('''
                CREATE TABLE show_piece
                (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        show_id INTEGER NOT NULL,
                        piece_id INTEGER NOT NULL,
                        FOREIGN KEY(piece_id) REFERENCES piece(id)
                        FOREIGN KEY(show_id) REFERENCES piece(id)
                );
            ''');
    print('tables created')

def InsPiece_Show( show_id, piece_id ):
    '''Insert new contact'''

    p = [ show_id, piece_id ]

    c.execute("INSERT INTO piece( show_id, piece_id ) VALUES(?,?)", p)

def InsShow( gallery_id, date_start, date_end ):
    '''Insert new contact'''

    p = [ gallery_id, date_start, date_end ]

    c.execute("INSERT INTO piece( gallery_id, date_start, date_end ) VALUES(?,?,?)", p)

def InsGallery( name, address, city, state, zip, phone ):
    '''Insert new contact'''

    p = [ name, address, city, state, zip, phone ]

    c.execute("INSERT INTO piece( name, address, city, state, zip, phone ) VALUES(?,?,?,?,?,?)", p)

def InsContact( address, city, state, zip, phone, gallery_id ):
    '''Insert new contact'''

    p = [ address, city, state, zip, phone, gallery_id ]

    c.execute("INSERT INTO piece( address, city, state, zip, phone, gallery_id ) VALUES(?,?,?,?,?,?)", p)

def InsPiece(title, medium, dimensions, signature_location, date, notes):
    '''Inserts a piece into piece table'''

    p = [ title, medium, dimensions, signature_location, date, notes ]

    c.execute("INSERT INTO piece(title, medium, dimensions, signature_location, date_completed, notes) VALUES(?,?,?,?,?,?)", p)

def InsSold():
    '''Inserts transaction into the sold table'''

    p = [ gallery_id, contacts_id, wholesale, gallery_percent, date_purchased, gallery.id,contacts.id ]

    c.execute("INSERT INTO sold(gallery_id, contacts_id, wholesale, gallery_percent, date_purchased, gallery_id,contacts_id) VALUES(?,?,?,?,?,?)", p)

def SelPiece_One():
        '''Selects the first piece from the database table piece'''
        c = conn.cursor()
        c.execute('SELECT * from piece')
        row = c.fetchone()
        for r in row:
            print(r)


