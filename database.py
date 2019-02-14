import sqlite3
from sqlite3 import Error


statement1 = '''CREATE TABLE IF NOT EXISTS user (
                            first_name TEXT NOT NULL,
                            last_name TEXT NOT NULL,
                            type NUMBER NOT NULL,
                            licence_number NUMBER PRIMARY KEY,
                            email TEXT NOT NULL,
                            password TEXT NOT NULL);'''

statement2 = '''INSERT OR IGNORE INTO user
                VALUES ('adriaan', 'van der valk', 0, 123456, 'jasper.v.d.valk@gmail.com', 'password123');
                '''

statement3 = 'SELECT * FROM user;'


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
        print('Successfully executed query')
        close_connection(connection)
    except Error as e:
        print(e)
