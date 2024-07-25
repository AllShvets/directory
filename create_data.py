from datetime import date, datetime
from random import choice

from faker import Faker
from transliterate import translit

faker = Faker('ru_RU')


def generate_age():
    random_date = faker.date_time()
    bith_date = random_date.strftime('%Y-%m-%d')
    return bith_date


def faker_person_create():
    b_date = generate_age()
    name_f = translit(faker.name(), language_code='ru', reversed=True)
    gender = ''
    if name_f[-1] == 'a':
        gender = 'Female'
    else:
        gender = 'Male'

    dict_person = {
        'full_name': name_f,
        'birthdate': b_date,
        'gender': gender
    }

    return dict_person


print(faker_person_create())