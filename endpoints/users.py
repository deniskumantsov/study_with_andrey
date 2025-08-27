import requests
from requests import Response
from config import BASE_URL


# Сделать обновление.
class UserRequest:
    """
    Класс для работы с эндпоинтами.
    Содержит методы для получения, создания, обновления и удаления пользователя.
    """

    BASE_ENDPOINT: str = "/users/"

    def __init__(self):
        self.base_url: str = BASE_URL


    def create_user_request(self, body: dict) -> Response:
        """
        Отправляет POST-запрос для создания нового пользователя.
        :param body: Тело запроса.
        :return: Объект Response.
        """
        response: Response = requests.post(f"{self.base_url}{self.BASE_ENDPOINT}", json=body)
        return response


    def get_user_request(self, user_id: int) -> Response:
        """
        Отправляет GET-запрос для получения информации о пользователе.
        :param user_id: ID пользователя.
        :return: Объект Response.
        """
        response: Response = requests.get(f"{self.base_url}{self.BASE_ENDPOINT}{user_id}")
        return response


    def delete_user_request(self, user_id: int) -> Response:
        """
        Отправляет DELETE-запрос для удаления пользователя по user_id.
        :param user_id: ID пользователя.
        :return: Объект Response.
        """
        response: Response = requests.delete(f"{self.base_url}{self.BASE_ENDPOINT}{user_id}")
        return response
