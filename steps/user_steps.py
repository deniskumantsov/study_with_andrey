import json

import allure

from checkers.common_checkers import CommonChecker
from checkers.user_checkers import UserChecker
from endpoints.user_request import UserRequest
from users import user_payload


class UserSteps:
    """
    Класс-обертка над UserRequest.
    Содержит бизнес шаги.
    """
    def __init__(self):
        self.request = UserRequest()
        self.payload = user_payload


    def get_users(self, expected_status: int = 200):
        """
        Получить список всех пользователей.

        :param expected_status: Ожидаемый статус-код.
        :return: Объект Response.
        """
        response = self.request.get_users_request()
        CommonChecker.check_status_code(response, expected_status)
        UserChecker.check_response_data_type(response)
        UserChecker.check_response_structure(response)
        return response

    @allure.step("Создать пользователя")
    def user_create(self, expected_status: int, **kwargs):
        """
        Создать пользователя.

        :param expected_status: Ожидаемый статус-код.
        :param kwargs: Параметры для конфигурации тела запроса.
        :return: Объект Response.
        """
        payload = self.payload.get_request_body_for_user(**kwargs)
        response = self.request.create_user_request(payload)
        CommonChecker.check_status_code(response, expected_status)
        return response


    def user_create_successful(self, **kwargs):
        """
        Создать пользователя.

        :param kwargs: Параметры для конфигурации тела запроса.
        :return: Объект Response.
        """
        response = self.user_create(expected_status=200, **kwargs)
        payload = json.loads(response.request.body)
        UserChecker.check_response_body(response, payload)
        return response


    def get_user_by_id(self, user_id: int, expected_status: int = 200):
        """
        Получить пользователя по ID.

        :param user_id: ID пользователя.
        :param expected_status: Ожидаемый статус-код.
        :return: Объект Response.
        """
        response = self.request.get_user_request(user_id)
        CommonChecker.check_status_code(response, expected_status)
        return response


    def update_user(self, user: dict, expected_status: int = 200, **kwargs):
        """
        Обновить данные пользователя по ID.

        :param user_id: ID пользователя.
        :param expected_status: Ожидаемый статус-код.
        :param kwargs: Параметры для конфигурации тела запроса.
        :return: Объект Response.
        """
        payload = self.payload.get_request_body_for_user_update(user, **kwargs)
        response = self.request.update_user_request(user.get("id"), payload)
        CommonChecker.check_status_code(response, expected_status)
        return response


    def delete_user_by_id(self, user_id: int):
        """
        Удалить пользователя по ID.

        :param user_id: ID пользователя.
        :return: Объект Response.
        """
        response = self.request.delete_user_request(user_id)
        CommonChecker.check_status_code(response, 200)
        return response