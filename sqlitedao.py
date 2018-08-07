import sqlite3
import sys

dbPath = ":memory:"
conn = sqlite3.connect(dbPath)
c = conn.cursor()

def CreateTables():
    ''' Takes a connection object and creates the tables needed for my database '''

    #Create piece table
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

def InsPiece(title, medium, dimensions, signature_location, date, notes):
    '''Inserts a piece into database table piece'''
    p = [title, medium, dimensions, signature_location, date, notes]

    c.execute("INSERT INTO piece(title, medium, dimensions, signature_location, date_completed, notes) VALUES(?,?,?,?,?,?)", p)

def SelPiece_One():
        '''Selects the first piece from the database table piece'''
        c = conn.cursor()
        c.execute('SELECT * from piece')
        row = c.fetchone()
        for r in row:
            print(r)



#(title,medium,dimensions,signature_location,date_completed,notes)
