import sqlite3
from sqlite3 import Error

statement0 = '''INSERT OR IGNORE INTO user VALUES (
'0', 
'Adriaan', 
'van der', 
'Valk', 
'1992-09-11', 
'Waalhaven Oostzijde 81', 
'Rotterdam', 
'3087BM', 
'0641433503', 
'jasper.v.d.valk@gmail.com', 
'password123', 
'123456', 
'2019-02-19');'''


statement1 = '''CREATE TABLE IF NOT EXISTS user (
                            type INTEGER NOT NULL,
                            forename TEXT NOT NULL,
                            infix TEXT NOT NULL,
                            surname TEXT NOT NULL,
                            date_of_birth TEXT NOT NULL,
                            address TEXT NOT NULL,
                            city TEXT NOT NULL,
                            post_code TEXT NOT NULL,
                            telephone_number TEXT NOT NULL,
                            email_address TEXT UNIQUE NOT NULL,
                            password TEXT NOT NULL,
                            knsa_licence_number TEXT PRIMARY KEY,
                            date_of_membership TEXT NOT NULL);'''

statement2 = '''CREATE TABLE IF NOT EXISTS weapon (
                            type TEXT NOT NULL,
                            owner TEXT NOT NULL,
                            PRIMARY KEY (weapon_type, owner),
                            FOREIGN KEY (owner) REFERENCES user (knsa_licence_number)
                            ON DELETE CASCADE ON UPDATE CASCADE);'''

statement3 = '''CREATE TABLE IF NOT EXISTS ammunition (
                            type TEXT PRIMARY KEY,
                            price REAL NOT NULL,
                            stock INTEGER);'''

statement4 = '''CREATE TABLE IF NOT EXISTS score_card (
                            type TEXT PRIMARY KEY,
                            price REAL NOT NULL,
                            stock INTEGER);'''

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
                            weapon_type TEXT NOT NULL,                           
                            card_type TEXT NOT NULL,
                            FOREIGN KEY (ammunition_type) REFERENCES ammunition (type)
                            ON DELETE NO ACTION ON UPDATE CASCADE,
                            FOREIGN KEY (shooter) REFERENCES user (knsa_licence_number)
                            ON DELETE NO ACTION ON UPDATE CASCADE,
                            FOREIGN KEY (weapon_type) REFERENCES weapon (type)
                            ON DELETE NO ACTION ON UPDATE CASCADE,
                            FOREIGN KEY (card_type) REFERENCES score_card (type)
                            ON DELETE NO ACTION ON UPDATE CASCADE);'''

statement6 = '''CREATE TABLE IF NOT EXISTS sale_score_card (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            date_sold TEXT NOT NULL,
                            quantity INTEGER NOT NULL,
                            type TEXT NOT NULL,
                            seller TEXT NOT NULL,
                            buyer TEXT NOT NULL,
                            price REAL NOT NULL,                            
                            FOREIGN KEY (type) REFERENCES score_card (type)
                            ON DELETE NO ACTION ON UPDATE CASCADE,
                            FOREIGN KEY (seller) REFERENCES user (knsa_licence_number)
                            ON DELETE NO ACTION ON UPDATE CASCADE,
                            FOREIGN KEY (buyer) REFERENCES user (knsa_licence_number)
                            ON DELETE NO ACTION ON UPDATE CASCADE,
                            FOREIGN KEY (price) REFERENCES score_card (price)
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
                            FOREIGN KEY (price) REFERENCES score_card (price)
                            ON DELETE NO ACTION ON UPDATE NO ACTION);'''


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


def execute_sql(sql):
    connection = create_connection()
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
        if 'SELECT' in sql:
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


'''execute_sql(statement1)
execute_sql(statement2)
execute_sql(statement3)
execute_sql(statement4)
execute_sql(statement5)
execute_sql(statement6)
execute_sql(statement7)
execute_sql(statement0)'''

result = execute_sql('SELECT knsa_licence_number, forename, infix, surname FROM user;')
print(result[0][1])

