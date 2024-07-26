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

    dict_person = [
        name_f,
        b_date,
        gender
    ]

    return dict_person


def generate_name_starting_with_F():
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

    list_person = [full_name, generate_age(), 'Male']
    return list_person

print(generate_name_starting_with_F())
