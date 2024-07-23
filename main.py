import sys
from database import DatabaseManager


def main(mode):
    db_manager = DatabaseManager()

    if mode == '1':
        db_manager.create_table()
    elif mode == '2':
        db_manager.create_entries()
    elif mode == '3':
        db_manager.fetch_employee_records()
    elif mode == '4':
        db_manager.fill_database()
    else:
        print("Неизвестный режим.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python main.py <режим>")
    else:
        main(sys.argv[1])
