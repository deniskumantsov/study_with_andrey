from faker import Faker
import random
from datetime import date, timedelta


faker = Faker("ru_RU")


def generate_valid_phone_number() -> int:
    """
    Генерирует валидный номер телефона пользователя.
    :return
    """
    phone_number = random.randint(10**9, 10**10-1)
    return phone_number


def generate_valid_firstname() -> str:
    """
    Генерирует валидное имя пользователя.
    :return
    """
    return faker.first_name()


def generate_valid_lastname() -> str:
    """
    Генерирует валидную фамилию пользователя.
    :return
    """
    return faker.last_name()


def generate_valid_patronymic() -> str:
    """
    Генерирует валидное отчество пользователя.
    :return
    """
    return faker.middle_name()


def generate_valid_patronymic_none() -> None:
    """
    Генерирует валидное отчество пользователя.
    :return
    """
    return None


def generate_valid_birthday() -> str:
    """
    Генерирует валидную дату рождения пользователя.
    :return
    """
    birthday = faker.date_of_birth(minimum_age=18, maximum_age=100)
    return birthday.isoformat()


def generate_valid_passport_serial() -> int:
    """
    Генерирует валидную серию паспорта пользователя.
    :return
    """
    passport_serial = random.randint(10**3, 10**4-1)
    return passport_serial


def generate_valid_passport_number() -> int:
    """
    Генерирует валидный номер паспорта пользователя.
    :return
    """
    passport_number = random.randint(10**5, 10**6-1)
    return passport_number

# Переделать
def generate_valid_password() -> str:
    """
    Генерирует валидный пароль пользователя.
    :return
    """
    password = "Qwerty!123"
    return password


def generate_birthday_exact_age(age: int) -> str:
    """
    Генерирует дату рождения для человека ровно age лет сегодня.
    :param age:
    :return:
    """
    today = date.today()
    birth_date = today.replace(year=today.year - age)
    return birth_date.isoformat()


def generate_birthday_age_yesterday(age: int) -> str:
    """
    Генерирует дату рождения для человека, которому исполнилось age лет вчера.
    :param age:
    :return:
    """
    today = date.today()
    birth_date = today.replace(year=today.year - age) - timedelta(days=1)
    return birth_date.isoformat()


def generate_birthday_age_tomorrow(age: int) -> str:
    """
    Генерирует дату рождения для человека, которому исполнится age лет завтра.
    :param age:
    :return:
    """
    today = date.today()
    birth_date = today.replace(year=today.year - age) + timedelta(days=1)
    return birth_date.isoformat()
