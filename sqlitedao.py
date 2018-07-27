import sqlite3
import sys

class SqliteDao:
'''Gives access to the database through a connection building function called Connection. Holds sql for insert, update, delete, and select queries.'''
    def Connection(self, dbPath=":memory:"):
        ''' Takes a database path as an argument and returns a connection object fort that database path '''

        conn = sqlite3.connect(dbPath)
        return conn

    def EndConnection(self,conn):
        conn.close()

    def addTables(self,conn):
        ''' Takes a connection object and creates the tables needed for my database '''

        c = conn.cursor()
        #Create piece table
        c.execute('''
                    CREATE TABLE piece
                    (
                    	id INTEGER PRIMARY KEY AUTOINCREMENT,
                    	title VARCHAR(100) NOT NULL,
                    	medium VARCHAR(100), 
                    	dimensions VARCHAR(100),
                    	signature_location VARCHAR(40),
                    	date_completed VARCHAR(100) NOT NULL,
                    	notes VARCHAR(100)
                    );
                ''')
        
        #Create sold table
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
        
        #Create contact table
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
        
        #Create gallery table
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
        
        #Create show table
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
        
        #Create show_piece table
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

    def insPiece(self,conn):
        ''' Inserts a piece into database table piece '''

        c = conn.cursor()
        c.execute(''' INSERT INTO piece(title,medium,dimensions,signature_location,date_completed,notes) VALUES('Anonymous Soldier','Oil','10x10','back left corner','10/10/10','some notes about the piece'); ''')

    def selPiece_One(self,conn):
        ''' selects the first piece from the database table piece '''
        c = conn.cursor()
        c.execute('SELECT * from piece')
        row = c.fetchone()
        print(row[0])
        print(row[1])
        print(row[2])
        print(row[3])
        print(row[4])
        print(row[5])

