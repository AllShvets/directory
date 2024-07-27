from faker import Faker
from transliterate import translit
import random
from datetime import datetime, timedelta

faker = Faker()


class Data:
    def generate_age(self):
        random_date = faker.date_of_birth(minimum_age=18, maximum_age=80)
        b_date = random_date.strftime('%Y-%m-%d')
        return b_date

    def faker_person_create(self):
        b_date = self.generate_age()
        last_name = translit(
            faker.last_name_male(),
            language_code='ru',
            reversed=True
        )
        first_name = translit(
            faker.first_name(),
            language_code='ru',
            reversed=True
        )
        patronymic = translit(
            faker.first_name(),
            language_code='ru',
            reversed=True
        )
        name_f = last_name + ' ' + first_name + ' ' + patronymic
        gender = ''
        if name_f[-1] == 'a':
            gender = 'Female'
        else:
            gender = 'Male'

        list_person = [name_f, b_date, gender]

        return list_person

    def generate_name_starting_with_F(self):
        last_name = translit(
            'Ф' + faker.last_name_male()[1:],
            language_code='ru',
            reversed=True
        )
        first_name = translit(
            faker.first_name_male(),
            language_code='ru',
            reversed=True
        )
        patronymic = translit(
            faker.first_name_male() + 'ович',
            language_code='ru',
            reversed=True
        )
        full_name = last_name + ' ' + first_name + ' ' + patronymic

        list_person = [full_name, self.generate_age(), 'Male']
        return list_person
