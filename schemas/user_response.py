from dataclasses import dataclass, asdict
from typing import Optional


@dataclass
class UserResponseSchema:
    """
    Структура ответа сервера при работе с пользователем.
    """
    phone_number: int
    firstname: str
    lastname: str
    patronymic: Optional[str]
    birthday: str
    passport_serial: int
    passport_number: int
    id: int