class Employee:
    def __init__(self, full_name, birthdate, gender):
        self.full_name = full_name
        self.birthdate = birthdate
        self.gender = gender

    def __str__(self):
        return f"{self.full_name}, {self.birthdate}, {self.gender}"
