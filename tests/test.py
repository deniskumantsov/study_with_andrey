import requests
from pydantic import BaseModel


base_url = "http://127.0.0.1:8000/users/"


class UserResponseModel(BaseModel):
    """
    Модель ответа от сервера.
    """
    phone_number: int
    firstname: str
    lastname: str
    patronymic: str | None
    birthday: str
    passport_serial: int
    passport_number: int
    id: int


def test_register_user():
    request_body = {
        "phone_number": 9539595679,
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

    response_body = response.json()
    print(response_body)

    # Валидируем ответ через Pydantic
    # Проверяем типы и наличие всех обязательных полей
    user = UserResponseModel(**response_body) # распаковка словаря в аргументы класса UserResponseModel

    # Проверяем, что поля запроса совпадают полями с ответом
    assert user.phone_number == request_body["phone_number"]
    assert user.firstname == request_body["firstname"]
    assert user.lastname == request_body["lastname"]
    assert user.patronymic == request_body["patronymic"]
    assert user.birthday == request_body["birthday"]
    assert user.passport_serial == request_body["passport_serial"]
    assert user.passport_number == request_body["passport_number"]

    # id автоматически проверяется как int через Pydantic
    assert isinstance(user.id, int)

