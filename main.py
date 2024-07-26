import sys
import click
import random
import string
from employee import Employee
from database import create_table, get_connection
from create_data import faker_person_create


@click.command()
@click.argument('mode')
@click.argument('additional_args', nargs=-1)
def main(mode, additional_args):
    if mode == '1':
        create_table()
        print('Таблица employees создана.')

    elif mode == '2':
        if len(additional_args) != 3:
            print('Пожалуйста, введите ФИО, дату рождения и пол')
        emp = Employee(
            additional_args[0],
            additional_args[1],
            additional_args[2]
        )
        with get_connection() as conn:
            emp.save_to_db(conn)
        print(f'Сотрудник {emp.full_name} добавлен в таблицу.')

    elif mode == '3':
        query = '''
        SELECT full_name, birthdate, gender
        FROM employees
        GROUP BY full_name
        '''
        with get_connection() as conn:
            cursor = conn.cursor()
            rows = cursor.execute(query).fetchall()
            for row in rows:
                employee_age = Employee(row[0], row[1], row[2]).calculate_age()
                result_string = (f'Имя: {row[0]}, Дата рождения: {row[1]}, '
                                 f'Пол: {row[2]}, '
                                 f'Кол-во полных лет: {employee_age}')
                print(result_string)

    elif mode == '4':
        data_package = []
        with get_connection() as conn:
            cursor = conn.cursor()
            query = "INSERT INTO employees (full_name, birthdate, gender) VALUES (?, ?, ?)"
            for _ in range(1000000):
                data_package.append(tuple(faker_person_create()))
                if len(data_package) >= 10000:  # Вставка батчами по 10,000 записей
                    cursor.executemany(query, data_package)
                    data_package.clear()  # Очистка списка для следующего батча
            # Вставляем оставшиеся данные
            if data_package:
                cursor.executemany(query, data_package)



if __name__ == '__main__':
    main()
