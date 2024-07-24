from datetime import datetime


class Employee:
    def __init__(self, full_name, birthdate, gender):
        self.full_name = full_name
        self.birthdate = datetime.strptime(birthdate, '%Y-%m-%d')
        self.gender = gender

    def calculate_age(self):
        today = datetime.today()
        return today.year - self.birthdate.year - (
            (today.month, today.day) <
            (self.birthdate.month, self.birthdate.day))

    def save_to_db(self, conn):
        with conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO employees (full_name, birthdate, gender) VALUES (?, ?, ?)",
                (self.full_name, self.birthdate.strftime('%Y-%m-%d'), self.gender)

            )
