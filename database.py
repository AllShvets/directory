import sqlite3
from models import Employee
from datetime import datetime


# создание
# заполнение
# вывод всех записей
# вывод записей по условию


class DatabaseManager:
    def __init__(self):
        self.conn = sqlite3.connect('employees.db')
        self.create_table()

    def create_table(self):
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS employees (
                    id INTEGER PRIMARY KEY,
                    full_name TEXT,
                    birthdate TEXT,
                    gender TEXT
                )
            ''')
        print('Таблица создана.')

    def create_entries(self, name, dirth_date, gender):
        employee = Employee(name, dirth_date, gender)
        with self.conn:
            self.conn.execute(
                '''INSERT INTO employees (full_name, birthdate, gender) VALUES (?, ?, ?)''',
                (employee.name, employee.birthdate, employee.gender)
            )
        print("Запись добавлена в таблицу.")

    def fill_database(self):
        employees = [
            Employee("Shvets Alexandra Igorevna", "1998-01-01", "Female"),
            Employee("Kasperskiy Fedor Ivanovich", "1963-02-21", "Male"),
            Employee("Guido Van Rossum", "1956-01-31", "Male"),
        ]
        with self.conn:
            self.conn.executemany('''
                INSERT INTO employees (full_name, birthdate, gender) VALUES (?, ?, ?)
            ''', [(emp.full_name, emp.birthdate, emp.gender) for emp in employees])
        print("Записи добавлены в таблицу.")

    def fetch_employee_records(self):
        query = '''
            SELECT
                full_name,
                birthdate,
                gender,
                (strftime('%Y', 'now') - strftime('%Y', birthdate) -
                (strftime('%m', 'now') < strftime('%m', birthdate) OR
                (strftime('%m', 'now') = strftime('%m', birthdate) AND strftime('%d', 'now') < strftime('%d', birthdate)))) ) AS age
            FROM
                employees
            ORDER BY
                full_name
        '''
        with self.conn:
            cursor = self.conn.execute(query)
            rows = cursor.fetchall()
            for row in rows:
                full_name, birthdate, gender, age = row
                print(f"ФИО: {full_name}, Дата рождения: {birthdate}, Пол: {gender}, Возраст: {age} полных лет")
