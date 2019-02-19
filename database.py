import sqlite3
from sqlite3 import Error


statement1 = '''CREATE TABLE IF NOT EXISTS member (
                            user_type INTEGER NOT NULL,
                            first_name TEXT NOT NULL,
                            infix TEXT NOT NULL,
                            surname TEXT NOT NULL,
                            date_of_birth TEXT NOT NULL,
                            address TEXT NOT NULL,
                            city TEXT NOT NULL,
                            post_code TEXT NOT NULL,
                            telephone_number INTEGER NOT NULL,
                            email_address TEXT UNIQUE NOT NULL,
                            password TEXT NOT NULL,
                            knsa_licence_number INTEGER PRIMARY KEY,
                            date_of_membership TEXT NOT NULL);'''

statement2 = '''CREATE TABLE IF NOT EXISTS weapon (
                            weapon_type TEXT NOT NULL,
                            owner INTEGER NOT NULL,
                            PRIMARY KEY (weapon_type, owner),
                            FOREIGN KEY (owner) REFERENCES member (knsa_licence_number)
                            ON DELETE CASCADE ON UPDATE CASCADE);'''

statement3 = '''CREATE TABLE IF NOT EXISTS ammunition (
                            ammunition_type TEXT PRIMARY KEY,
                            price REAL NOT NULL,
                            stock INTEGER);'''

statement4 = '''CREATE TABLE IF NOT EXISTS score_card (
                            score_card_type TEXT PRIMARY KEY,
                            price REAL NOT NULL,
                            stock INTEGER);'''

statement5 = '''CREATE TABLE IF NOT EXISTS score (
                            score_id INTEGER PRIMARY KEY AUTOINCREMENT,                            
                            shot_one INTEGER NOT NULL,
                            shot_two INTEGER NOT NULL,
                            shot_three INTEGER NOT NULL,
                            shot_four INTEGER NOT NULL,
                            shot_five INTEGER NOT NULL,
                            date_score TEXT NOT NULL,
                            ammunition_type TEXT NOT NULL,                            
                            shooter INTEGER NOT NULL,                            
                            weapon_type TEXT NOT NULL,                           
                            card_type TEXT NOT NULL,
                            FOREIGN KEY (card_type) REFERENCES score_card (card_type)
                            ON DELETE NO ACTION ON UPDATE CASCADE,
                            FOREIGN KEY (ammunition_type) REFERENCES ammunition (ammunition_type)
                            ON DELETE NO ACTION ON UPDATE CASCADE,
                            FOREIGN KEY (shooter) REFERENCES member (knsa_licence_number)
                            ON DELETE NO ACTION ON UPDATE CASCADE,
                            FOREIGN KEY (weapon_type) REFERENCES weapon (weapon_type)
                            ON DELETE NO ACTION ON UPDATE CASCADE);'''

statement6 = '''CREATE TABLE IF NOT EXISTS sale_score_card (
                            sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            score_card_type TEXT NOT NULL,
                            date_sold TEXT NOT NULL,
                            quantity INTEGER NOT NULL,
                            seller INTEGER NOT NULL,
                            buyer INTEGER NOT NULL,
                            price REAL NOT NULL,                            
                            FOREIGN KEY (card_type) REFERENCES score_card (card_type)
                            ON DELETE NO ACTION ON UPDATE NO ACTION,
                            FOREIGN KEY (seller) REFERENCES member (knsa_licence_number)
                            ON DELETE NO ACTION ON UPDATE CASCADE,
                            FOREIGN KEY (buyer) REFERENCES member (knsa_licence_number)
                            ON DELETE NO ACTION ON UPDATE CASCADE,
                            FOREIGN KEY (price) REFERENCES score_card (price)
                            ON DELETE NO ACTION ON UPDATE NO ACTION);'''

statement7 = '''CREATE TABLE IF NOT EXISTS sale_ammunition (
                            sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            ammunition_type TEXT NOT NULL,
                            date_sold NOT NULL,
                            quantity INTEGER NOT NULL,
                            seller INTEGER NOT NULL,
                            buyer INTEGER NOT NULL,
                            price REAL NOT NULL,
                            FOREIGN KEY (score_cardammunition_type) REFERENCES ammunition (ammunition_type)
                            ON DELETE NO ACTION ON UPDATE NO ACTION,
                            FOREIGN KEY (seller) REFERENCES member (knsa_licence_number)
                            ON DELETE NO ACTION ON UPDATE CASCADE,
                            FOREIGN KEY (buyer) REFERENCES member (knsa_licence_number)
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
    print('Connection closed')


def execute_sql(sql):
    connection = create_connection()
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
        if 'SELECT' in sql:
            rows = cursor.fetchall()
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
execute_sql(statement7)'''
