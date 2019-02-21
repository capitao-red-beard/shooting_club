import sqlite3
from sqlite3 import Error


def create_connection():
    try:
        connection = sqlite3.connect('shooting_club')
        print('Connected to database. SQLite: ' + sqlite3.version)
        return connection
    except Error as e:
        print(e)


def close_connection(connection):
    connection.close()
    print('Connection closed. SQLite: ' + sqlite3.version)


def execute_sql(sql, *args):
    connection = create_connection()
    try:
        cursor = connection.cursor()
        cursor.execute(sql, *args)
        if sql.lstrip().upper().startswith('SELECT'):
            rows = cursor.fetchall()
            close_connection(connection)
            return rows
        else:
            connection.commit()
            print('Successfully executed and committed SQL')
        close_connection(connection)
        return 'success'
    except Error as e:
        print(e)
        close_connection(connection)


statement0 = '''INSERT INTO user (
type, 
first_name,
last_name, 
date_of_birth, 
address, 
city, 
post_code, 
telephone_number, 
email_address, 
password, 
knsa_licence_number, 
date_of_membership
) VALUES (
'0', 
'adriaan',  
'van der valk', 
'1992-09-11', 
'waalhaven oostzijde 81', 
'rotterdam', 
'3087bm', 
'0641433503', 
'jasper.v.d.valk@gmail.com', 
'password123', 
'123456', 
'2019-02-19');'''

statement13 = '''INSERT INTO user (
type, 
first_name, 
last_name, 
date_of_birth, 
address, 
city, 
post_code, 
telephone_number, 
email_address, 
password, 
knsa_licence_number, 
date_of_membership
) VALUES (
'1', 
'john', 
'doe', 
'1999-12-31', 
'2 thames crescent', 
'maidenhead', 
'sl68ey', 
'07704482570', 
'john.doe@gmail.com', 
'password123', 
'654321', 
'2019-02-20');'''

statement8 = '''INSERT INTO scorecard (type, price, stock) VALUES ('competition', 0.30, 100)'''
statement9 = '''INSERT INTO scorecard (type, price, stock) VALUES ('regular', 0.30, 100)'''

statement10 = '''INSERT INTO ammunition (type, price, stock) VALUES ('cci', 0.12, 100)'''
statement11 = '''INSERT INTO ammunition (type, price, stock) VALUES ('eley', 0.13, 100)'''
statement12 = '''INSERT INTO ammunition (type, price, stock) VALUES ('rws', 0.14, 100)'''

statement14 = '''INSERT INTO firearm (type, owner) VALUES ('pistol', '123456')'''
statement15 = '''INSERT INTO firearm (type, owner) VALUES ('shotgun', '123456')'''
statement16 = '''INSERT INTO firearm (type, owner) VALUES ('pistol', '654321')'''


statement1 = '''CREATE TABLE IF NOT EXISTS user (
                            type INTEGER NOT NULL,
                            first_name TEXT NOT NULL,
                            last_name TEXT NOT NULL,
                            date_of_birth TEXT NOT NULL,
                            address TEXT NOT NULL,
                            city TEXT NOT NULL,
                            post_code TEXT NOT NULL,
                            telephone_number TEXT NOT NULL,
                            email_address TEXT UNIQUE NOT NULL,
                            password TEXT NOT NULL,
                            knsa_licence_number TEXT PRIMARY KEY,
                            date_of_membership TEXT NOT NULL);'''

statement2 = '''CREATE TABLE IF NOT EXISTS firearm (
                            type TEXT NOT NULL,
                            owner TEXT NOT NULL,
                            PRIMARY KEY (type, owner),
                            FOREIGN KEY (owner) REFERENCES user (knsa_licence_number)
                            ON DELETE CASCADE ON UPDATE CASCADE);'''

statement3 = '''CREATE TABLE IF NOT EXISTS ammunition (
                            type TEXT PRIMARY KEY,
                            price REAL NOT NULL,
                            stock INTEGER NOT NULL);'''

statement4 = '''CREATE TABLE IF NOT EXISTS scorecard (
                            type TEXT PRIMARY KEY,
                            price REAL NOT NULL,
                            stock INTEGER NOT NULL);'''

statement5 = '''CREATE TABLE IF NOT EXISTS score (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,                            
                            shot_one INTEGER NOT NULL,
                            shot_two INTEGER NOT NULL,
                            shot_three INTEGER NOT NULL,
                            shot_four INTEGER NOT NULL,
                            shot_five INTEGER NOT NULL,
                            date_score TEXT NOT NULL,
                            ammunition_type TEXT NOT NULL,                            
                            shooter TEXT NOT NULL,                            
                            firearm_type TEXT NOT NULL,                           
                            scorecard_type TEXT NOT NULL,
                            FOREIGN KEY (ammunition_type) REFERENCES ammunition (type)
                            ON DELETE NO ACTION ON UPDATE CASCADE,
                            FOREIGN KEY (shooter) REFERENCES user (knsa_licence_number)
                            ON DELETE NO ACTION ON UPDATE CASCADE,
                            FOREIGN KEY (firearm_type) REFERENCES firearm (type)
                            ON DELETE NO ACTION ON UPDATE CASCADE,
                            FOREIGN KEY (scorecard_type) REFERENCES scorecard (type)
                            ON DELETE NO ACTION ON UPDATE CASCADE);'''

statement6 = '''CREATE TABLE IF NOT EXISTS sale_scorecard (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            date_sold TEXT NOT NULL,
                            quantity INTEGER NOT NULL,
                            type TEXT NOT NULL,
                            seller TEXT NOT NULL,
                            buyer TEXT NOT NULL,
                            price REAL NOT NULL,                            
                            FOREIGN KEY (type) REFERENCES scorecard (type)
                            ON DELETE NO ACTION ON UPDATE CASCADE,
                            FOREIGN KEY (seller) REFERENCES user (knsa_licence_number)
                            ON DELETE NO ACTION ON UPDATE CASCADE,
                            FOREIGN KEY (buyer) REFERENCES user (knsa_licence_number)
                            ON DELETE NO ACTION ON UPDATE CASCADE,
                            FOREIGN KEY (price) REFERENCES scorecard (price)
                            ON DELETE NO ACTION ON UPDATE NO ACTION);'''

statement7 = '''CREATE TABLE IF NOT EXISTS sale_ammunition (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            date_sold TEXT NOT NULL,
                            quantity INTEGER NOT NULL,
                            type TEXT NOT NULL,
                            seller TEXT NOT NULL,
                            buyer TEXT NOT NULL,
                            price REAL NOT NULL,
                            FOREIGN KEY (type) REFERENCES ammunition (type)
                            ON DELETE NO ACTION ON UPDATE CASCADE,
                            FOREIGN KEY (seller) REFERENCES user (knsa_licence_number)
                            ON DELETE NO ACTION ON UPDATE CASCADE,
                            FOREIGN KEY (buyer) REFERENCES user (knsa_licence_number)
                            ON DELETE NO ACTION ON UPDATE CASCADE,
                            FOREIGN KEY (price) REFERENCES ammunition (price)
                            ON DELETE NO ACTION ON UPDATE NO ACTION);'''

'''execute_sql(statement1)
execute_sql(statement2)
execute_sql(statement3)
execute_sql(statement4)
execute_sql(statement5)
execute_sql(statement6)
execute_sql(statement7)
execute_sql(statement0)
execute_sql(statement8)
execute_sql(statement9)
execute_sql(statement10)
execute_sql(statement11)
execute_sql(statement12)
execute_sql(statement13)
execute_sql(statement14)
execute_sql(statement15)
execute_sql(statement16)'''

