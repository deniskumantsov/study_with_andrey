from dataclasses import dataclass, field, asdict
from typing import Optional
from utils.generators import generate_valid_phone_number, generate_valid_firstname, generate_valid_lastname, \
    generate_valid_patronymic, generate_valid_birthday, generate_valid_passport_serial, generate_valid_passport_number, \
    generate_valid_password


def get_request_body_for_user(**kwargs) -> dict:
    """
    Конфигурирует тело запроса для создания пользователя.
    :return: Словарь с полями:
        - phone_number (int)
        - firstname (str)
        - lastname (str)
        - patronymic (str)
        - birthday (str)
        - passport_serial (int)
        - passport_number (int)
        - password (str)
    """
    payload = {
        "phone_number": generate_valid_phone_number(),
        "firstname": generate_valid_firstname(),
        "lastname": generate_valid_lastname(),
        "patronymic": generate_valid_patronymic(),
        "birthday": generate_valid_birthday(),
        "passport_serial": generate_valid_passport_serial(),
        "passport_number": generate_valid_passport_number(),
        "password": generate_valid_password(),
    }

    for key, value in kwargs.items():
        payload[key] = value

    return payload




# Пример реализации через dataclass
# @dataclass
# class UserResponseSchema:
#     """
#     Структура ответа сервера при работе с пользователем.
#     """
#     phone_number: int = field(default_factory=generate_valid_phone_number)
#     firstname: str = field(default_factory=generate_valid_firstname)
#     lastname: str = field(default_factory=generate_valid_lastname)
#     patronymic: Optional[str] = None
#     birthday: str = field(default_factory=generate_valid_birthday)
#     passport_serial: int = field(default_factory=generate_valid_passport_serial)
#     passport_number: int = field(default_factory=generate_valid_passport_number)
#     password: str = field(default_factory=generate_valid_password)
#
#     def as_payload(self):
#         if self.patronymic:
#             return asdict(self)
#         else:
#             payload = asdict(self)
#             del payload["patronymic"]
#             return payload
#
#
# if __name__ == "__main__":
#     payload = UserResponseSchema(phone_number="denis molodec")
#     payload.title="andrey molodec"
#     print(payload.title)
#     print(payload.as_payload())