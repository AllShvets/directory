import sqlite3


# создание
# заполнение
# вывод всех записей
# вывод записей по условию

DATABASE_NAME = 'employees.db'


def create_table():
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


def get_connection():
    return sqlite3.connect(DATABASE_NAME)
