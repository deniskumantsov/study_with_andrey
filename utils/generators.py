from faker import Faker
import random


faker = Faker("ru_RU")


def generate_valid_phone_number() -> int:
    """
    Генерирует валидный номер телефона пользователя.
    :return
    """
    phone_number = random.randint(10**9, 10**10-1)
    return phone_number
print(generate_valid_phone_number())


def generate_valid_firstname() -> str:
    """
    Генерирует валидное имя пользователя.
    :return
    """
    return faker.first_name()
print(generate_valid_firstname())


def generate_valid_lastname() -> str:
    """
    Генерирует валидную фамилию пользователя.
    :return
    """
    return faker.last_name()
print(generate_valid_lastname())


def generate_valid_patronymic() -> str:
    """
    Генерирует валидное отчество пользователя.
    :return
    """
    return faker.middle_name()
print(generate_valid_patronymic())


def generate_valid_patronymic_none() -> None:
    """
        Генерирует валидное отчество пользователя.
        :return
        """
    return None
print(generate_valid_patronymic_none())


def generate_valid_birthday() -> str:
    """
    Генерирует валидную дату рождения пользователя.
    :return
    """
    birthday = faker.date_of_birth(minimum_age=18, maximum_age=100)
    return birthday.isoformat()
print(generate_valid_birthday())


def generate_valid_passport_serial() -> int:
    """
    Генерирует валидную серию паспорта пользователя.
    :return
    """
    passport_serial = random.randint(10**3, 10**4-1)
    return passport_serial
print(generate_valid_passport_serial())


def generate_valid_passport_number() -> int:
    """
    Генерирует валидный номер паспорта пользователя.
    :return
    """
    passport_number = random.randint(10**5, 10**6-1)
    return passport_number
print(generate_valid_passport_number())

# Переделать
def generate_valid_password() -> str:
    """
    Генерирует валидный пароль пользователя.
    :return
    """
    password = "Qwerty!123"
    return password
print(generate_valid_password())