import sqlite3

DATABASE_NAME = 'employees.db'


class Database:
    def create_table(self):
        with sqlite3.connect(DATABASE_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                full_name TEXT NOT NULL,
                birthdate DATE NOT NULL,
                gender TEXT NOT NULL
            )
            ''')
            conn.commit()

    def get_connection(self):
        return sqlite3.connect(DATABASE_NAME)
