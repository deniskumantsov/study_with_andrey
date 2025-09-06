import requests
from requests import Response
from config import BASE_URL


class UserRequest:
    """
    Класс для работы с endpoints.
    Содержит методы для получения, создания, обновления и удаления пользователя.
    """

    BASE_ENDPOINT: str = "/users/"

    def __init__(self):
        self.base_url: str = BASE_URL


    def get_users_request(self) -> Response:
        """
        Отправить GET-запрос для получения списка всех пользователей.

        :return: Объект Response.
        """
        response: Response = requests.get(f"{self.base_url}{self.BASE_ENDPOINT}")
        return response


    def create_user_request(self, body: dict) -> Response:
        """
        Отправить POST-запрос для создания нового пользователя.

        :param body: Тело запроса.
        :return: Объект Response.
        """
        response: Response = requests.post(f"{self.base_url}{self.BASE_ENDPOINT}", json=body)
        return response


    def get_user_request(self, user_id: int) -> Response:
        """
        Отправить GET-запрос для получения информации о пользователе.

        :param user_id: ID пользователя.
        :return: Объект Response.
        """
        response: Response = requests.get(f"{self.base_url}{self.BASE_ENDPOINT}{user_id}")
        return response


    def update_user_request(self, user_id: int, body: dict) -> Response:
        """
        Отправить PATCH-запрос для обновления данных пользователя.

        :param user_id: ID пользователя.
        :param body: Тело запроса.
        :return: Объект Response.
        """
        response: Response = requests.patch(f"{self.base_url}{self.BASE_ENDPOINT}{user_id}",json=body)
        return response


    def delete_user_request(self, user_id: int) -> Response:
        """
        Отправить DELETE-запрос для удаления пользователя.

        :param user_id: ID пользователя.
        :return: Объект Response.
        """
        response: Response = requests.delete(f"{self.base_url}{self.BASE_ENDPOINT}{user_id}")
        return response