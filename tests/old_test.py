import requests
import pytest
from pydantic import BaseModel
from utils.phone_number_generator import generate_valid_phone_number, generate_invalid_phone_number_nine, \
    generate_invalid_phone_number_eleven, generate_invalid_phone_number_str, generate_invalid_phone_number_none


base_url = "http://127.0.0.1:8000/users/"


class UserResponse(BaseModel):
    phone_number: int
    firstname: str
    lastname: str
    patronymic: str | None
    birthday: str
    passport_serial: int
    passport_number: int
    id: int


def test_register_user_with_patronymic():
    request_body = { # Убрать дублирование
        "phone_number": generate_valid_phone_number(),
        "firstname": "Денис",
        "lastname": "Куманцов",
        "patronymic": "Игоревич",
        "birthday": "1999-09-03",
        "passport_serial": 1234,
        "passport_number": 567890,
        "password": "Qwerty!123"
    }

    response = requests.post(base_url, json=request_body)
    assert response.status_code == 200

    assert response.headers["Content-Type"] == "application/json"

    response_body = response.json()
    user = UserResponse(**response_body)

    assert user.phone_number == request_body["phone_number"]
    assert user.firstname == request_body["firstname"]
    assert user.lastname == request_body["lastname"]
    assert user.patronymic == request_body["patronymic"]
    assert user.birthday == request_body["birthday"]
    assert user.passport_serial == request_body["passport_serial"]
    assert user.passport_number == request_body["passport_number"]


def test_register_user_without_patronymic():
    request_body = {
        "phone_number": generate_valid_phone_number(),
        "firstname": "Денис",
        "lastname": "Куманцов",
        "patronymic": None,
        "birthday": "1999-09-03",
        "passport_serial": 1234,
        "passport_number": 567890,
        "password": "Qwerty!123"
    }

    response = requests.post(base_url, json=request_body)
    assert response.status_code == 200

    assert response.headers["Content-Type"] == "application/json"

    response_body = response.json()
    user = UserResponse(**response_body)

    assert user.phone_number == request_body["phone_number"]
    assert user.firstname == request_body["firstname"]
    assert user.lastname == request_body["lastname"]
    assert user.patronymic == request_body["patronymic"]
    assert user.birthday == request_body["birthday"]
    assert user.passport_serial == request_body["passport_serial"]
    assert user.passport_number == request_body["passport_number"]


@pytest.mark.parametrize("phone_number, expected_status", [
    (generate_invalid_phone_number_nine, 422),
    (generate_invalid_phone_number_eleven, 422),
    (generate_invalid_phone_number_str, 422),
    (generate_invalid_phone_number_none, 422),
])
def test_register_user_with_invalid_phone_number(phone_number, expected_status):
    phone = phone_number()
    request_body = {
        "phone_number": phone,
        "firstname": "Денис",
        "lastname": "Куманцов",
        "patronymic": "Игоревич",
        "birthday": "1999-09-03",
        "passport_serial": 1234,
        "passport_number": 567890,
        "password": "Qwerty!123"
    }

    response = requests.post(base_url, json=request_body)
    assert response.status_code == expected_status


def test_register_user_with_non_unique_phone_number():
    phone = generate_valid_phone_number()

    request_body = {
        "phone_number": phone,
        "firstname": "Денис",
        "lastname": "Куманцов",
        "patronymic": "Игоревич",
        "birthday": "1999-09-03",
        "passport_serial": 1234,
        "passport_number": 567890,
        "password": "Qwerty!123"
    }

    response_first = requests.post(base_url, json=request_body)
    assert response_first.status_code == 200
    response_second = requests.post(base_url, json=request_body)
    assert response_second.status_code == 422


def test_register_user_with_space_in_phone_number():
    request_body = {
        "phone_number":  generate_invalid_phone_number_nine() ,
        "firstname": "Денис",
        "lastname": "Куманцов",
        "patronymic": "Игоревич",
        "birthday": "1999-09-03",
        "passport_serial": 1234,
        "passport_number": 567890,
        "password": "Qwerty!123"
    }

    response = requests.post(base_url, json=request_body)
    assert response.status_code == 422


@pytest.mark.parametrize("firstname, expected_status", [
    ("a" * 1, 422),
    ("a" * 2, 200),
    ("a" * 3, 200),
    ("a" * 25, 200),
    ("a" * 254, 200),
    ("a" * 255, 200),
    ("a" * 256, 422),
    (None, 422),
    (123, 422),
    ("Лика123", 422),
    ("Лика!", 422),
    ("Лика&", 422),
    ("Denis", 422),
    ("Denis123", 422),
    ("Denis!", 422),
    ("Denis&", 422),
    (" Лика", 422),
    ("Ли ка", 422),
    ("Лика ", 422),
])
def test_register_user_firstname(firstname, expected_status): # Добавить типизацию и описание
    request_body = {
        "phone_number": generate_valid_phone_number(),
        "firstname": firstname,
        "lastname": "Куманцов",
        "patronymic": "Игоревич",
        "birthday": "1999-09-03",
        "passport_serial": 1234,
        "passport_number": 567890,
        "password": "Qwerty!123"
    }

    response = requests.post(base_url, json=request_body)
    assert response.status_code == expected_status


@pytest.mark.parametrize("lastname, expected_status", [
    ("a" * 1, 422),
    ("a" * 2, 200),
    ("a" * 3, 200),
    ("a" * 25, 200),
    ("a" * 254, 200),
    ("a" * 255, 200),
    ("a" * 256, 422),
    (None, 422),
    (123, 422),
    ("Петров-Сидоров", 200),
    ("Петров!", 422),
    ("Петров123", 422),
    ("Петров&", 422),
    ("Petrov", 422),
    ("  Петров", 422),
    ("Петров Сидоров", 200),
    ("Петров ", 422),
])
def test_register_user_lastname(lastname, expected_status):
    request_body = {
        "phone_number": generate_valid_phone_number(),
        "firstname": "Денис",
        "lastname": lastname,
        "patronymic": "Игоревич",
        "birthday": "1999-09-03",
        "passport_serial": 1234,
        "passport_number": 567890,
        "password": "Qwerty!123"
    }

    response = requests.post(base_url, json=request_body)
    assert response.status_code == expected_status


@pytest.mark.parametrize("patronymic, expected_status", [
    ("a" * 1, 422),
    ("a" * 2, 422),
    ("a" * 3, 200),
    ("a" * 25, 200),
    ("a" * 254, 200),
    ("a" * 255, 200),
    ("a" * 256, 422),
    (123, 422),
    ("Игоревич!", 422),
    ("Игоревич123", 422),
    ("Игоревич&", 422),
    ("Petrovich", 422),
    (" Игоревич", 422),
    ("Иго ревич", 200),
    ("Игоревич ", 422),
])
def test_register_user_with_various_patronymic(patronymic, expected_status):
    request_body = {
        "phone_number": generate_valid_phone_number(),
        "firstname": "Денис",
        "lastname": "Куманцов",
        "patronymic": patronymic,
        "birthday": "1999-09-03",
        "passport_serial": 1234,
        "passport_number": 567890,
        "password": "Qwerty!123"
    }

    response = requests.post(base_url, json=request_body)
    assert response.status_code == expected_status


@pytest.mark.parametrize("birthday, expected_status", [
    (None, 422),
    ("", 422),
    ("2010-08-02", 422), # 15 лет
    ("2009-08-02", 200), # 16 лет
    ("1999-08-02", 200), # 26 лет
    ("1925-08-02", 422), # 100 лет
    ("1999-09-03!", 422),
    ("1999-09-0!", 422),
    ("1999-09-03&", 422),
    ("1999-09-03ааа", 422),
    ("1999.09.03", 422),
    ("1999/09/03", 422),
    ("1999&09&03", 422),
    ("0000-00-00", 422),
    ("2020-00-12", 422),
    ("2021-12-00", 422),
    ("0000-01-12", 422),
    ("1970-01-01", 200),
    ("9999-99-99", 422),
    ("9999-12-01", 422),
    ("2025-99-01", 422),
    ("2025-12-99", 422),
    ("2025-02-31", 422),
    ("2025-15-31", 422),
    ("2000-15-32", 422),
    (" 1999-09-03 ", 422),
    (123, 422),
])
def test_register_user_with_various_birthdays(birthday, expected_status):
    request_body = {
        "phone_number": generate_valid_phone_number(),
        "firstname": "Денис",
        "lastname": "Куманцов",
        "patronymic": "Игоревич",
        "birthday": birthday,
        "passport_serial": 1234,
        "passport_number": 567890,
        "password": "Qwerty!123"
    }

    response = requests.post(base_url, json=request_body)
    assert response.status_code == expected_status