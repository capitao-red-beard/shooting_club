import sqlite3
from sqlite3 import Error


def create_connection():
    try:
        connection = sqlite3.connect('shooting_club')
        connection.execute('PRAGMA foreign_keys = 1')
        print('Connected to database. SQLite: ' + sqlite3.version)
        return connection
    except Error as e:
        print(e)


def close_connection(connection):
    try:
        connection.close()
        print('Connection closed. SQLite: ' + sqlite3.version)
    except Error as e:
        print(e)


def execute_sql(sql, *args):
    print(sql)
    print(args)
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


statement1 = '''CREATE TABLE IF NOT EXISTS user (
                            type INTEGER NOT NULL,
                            first_name TEXT NOT NULL,
                            last_name TEXT NOT NULL,
                            date_of_birth INTEGER NOT NULL,
                            address TEXT NOT NULL,
                            city TEXT NOT NULL,
                            post_code TEXT NOT NULL,
                            telephone_number TEXT NOT NULL,
                            email_address TEXT UNIQUE,
                            password TEXT,
                            knsa_licence_number INTEGER PRIMARY KEY,
                            date_of_membership INTEGER NOT NULL);'''

statement2 = '''CREATE TABLE IF NOT EXISTS firearm (
                            type TEXT PRIMARY KEY);'''

statement8 = '''CREATE TABLE IF NOT EXISTS discipline (
                            type TEXT PRIMARY KEY);'''

statement9 = '''CREATE TABLE IF NOT EXISTS rank (
                            user INTEGER NOT NULL,
                            discipline TEXT NOT NULL,
                            class TEXT NOT NULL,
                            FOREIGN KEY (user) REFERENCES user (knsa_licence_number)
                            ON DELETE NO ACTION ON UPDATE CASCADE,
                            FOREIGN KEY (discipline) REFERENCES discipline (type)
                            ON DELETE NO ACTION ON UPDATE CASCADE,
                            PRIMARY KEY (user, discipline, class));'''

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
                            card_one_shot_one INTEGER NOT NULL,
                            card_one_shot_two INTEGER NOT NULL,
                            card_one_shot_three INTEGER NOT NULL,
                            card_one_shot_four INTEGER NOT NULL,
                            card_one_shot_five INTEGER NOT NULL,
                            card_one_total INTEGER NOT NULL,
                            card_two_shot_one INTEGER NOT NULL,
                            card_two_shot_two INTEGER NOT NULL,
                            card_two_shot_three INTEGER NOT NULL,
                            card_two_shot_four INTEGER NOT NULL,
                            card_two_shot_five INTEGER NOT NULL,
                            card_two_total INTEGER NOT NULL,
                            date_score INTEGER NOT NULL,                           
                            shooter INTEGER NOT NULL,                            
                            firearm_type TEXT NOT NULL,
                            discipline_type TEXT NOT NULL,                           
                            FOREIGN KEY (shooter) REFERENCES user (knsa_licence_number)
                            ON DELETE NO ACTION ON UPDATE CASCADE,
                            FOREIGN KEY (firearm_type) REFERENCES firearm (type)
                            ON DELETE NO ACTION ON UPDATE CASCADE,
                            FOREIGN KEY (discipline_type) REFERENCES discipline (type));'''

statement6 = '''CREATE TABLE IF NOT EXISTS sale_scorecard (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            date_sold INTEGER NOT NULL,
                            quantity INTEGER NOT NULL,
                            type TEXT NOT NULL,
                            seller INTEGER NOT NULL,
                            buyer INTEGER NOT NULL,
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
                            date_sold INTEGER NOT NULL,
                            quantity INTEGER NOT NULL,
                            type TEXT NOT NULL,
                            seller INTEGER NOT NULL,
                            buyer INTEGER NOT NULL,
                            price REAL NOT NULL,
                            FOREIGN KEY (type) REFERENCES ammunition (type)
                            ON DELETE NO ACTION ON UPDATE CASCADE,
                            FOREIGN KEY (seller) REFERENCES user (knsa_licence_number)
                            ON DELETE NO ACTION ON UPDATE CASCADE,
                            FOREIGN KEY (buyer) REFERENCES user (knsa_licence_number)
                            ON DELETE NO ACTION ON UPDATE CASCADE,
                            FOREIGN KEY (price) REFERENCES ammunition (price)
                            ON DELETE NO ACTION ON UPDATE NO ACTION);'''

'''
execute_sql(statement1)
execute_sql(statement2)
execute_sql(statement3)
execute_sql(statement4)
execute_sql(statement5)
execute_sql(statement6)
execute_sql(statement7)
'''
