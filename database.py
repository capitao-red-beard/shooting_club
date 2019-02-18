import sqlite3
from sqlite3 import Error


statement1 = '''CREATE TABLE IF NOT EXISTS user (
                            type NUMBER NOT NULL,
                            first_name TEXT NOT NULL,
                            infix TEXT NOT NULL,
                            surname TEXT NOT NULL,
                            date_of_birth DATE NOT NULL,
                            address TEXT NOT NULL,
                            city TEXT NOT NULL,
                            post_code TEXT NOT NULL,
                            telephone_number NUMBER NOT NULL,
                            email_address TEXT UNIQUE NOT NULL,
                            password TEXT NOT NULL,
                            knsa_licence_number NUMBER PRIMARY KEY,
                            date_of_membership DATE NOT NULL);'''

statement2 = '''INSERT OR IGNORE INTO user
                VALUES ();
                '''

statement3 = 'SELECT * FROM user;'

statement4 = '''CREATE TABLE IF NOT EXISTS weapon (
                            weapon TEXT PRIMARY KEY);'''


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


# execute_sql(statement4)
