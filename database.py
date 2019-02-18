import sqlite3
from sqlite3 import Error


statement1 = '''CREATE TABLE IF NOT EXISTS user (
                            type NUMBER NOT NULL,
                            voor_naam TEXT NOT NULL,
                            tussenvoegsel TEXT NOT NULL,
                            achter_naam TEXT NOT NULL,
                            geboorte_datum DATE NOT NULL,
                            telefoon_nummer NUMBER NOT NULL,
                            adres TEXT NOT NULL,
                            woonplaats TEXT NOT NULL,
                            postcode TEXT NOT NULL,
                            email_adres TEXT NOT NULL,
                            wachtwoord TEXT NOT NULL,
                            knsa_licentie_nummer NUMBER NOT NULL,
                            ingang_maatschap DATE NOT NULL);'''

statement2 = '''INSERT OR IGNORE INTO user
                VALUES ();
                '''

statement3 = 'SELECT * FROM user;'

statement4 = '''CREATE TABLE IF NOT EXISTS wapen (
                            wapen TEXT PRIMARY KEY);'''


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
