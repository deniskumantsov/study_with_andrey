from pydantic import BaseModel


class UserResponseSchema(BaseModel):
    """
    Класс, описывающий структуру ответа сервера при работе с пользователем.
    Используется для валидации и проверки того, что возвращает сервер.
    """
    phone_number: int
    firstname: str
    lastname: str
    patronymic: str | None
    birthday: str
    passport_serial: int
    passport_number: int
    id: int