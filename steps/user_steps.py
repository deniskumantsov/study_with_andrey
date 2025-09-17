import json
import allure
from checkers.common_checkers import CommonChecker
from checkers.user_checkers import UserChecker
from endpoints.user_request import UserRequest
from users import user_payload


# PomoikaCollector:
#
#     def add():
#         pass
#
#     def delete():
#         pass
#

class UserSteps:
    """
    Класс-обертка над UserRequest.
    Содержит бизнес шаги.
    """
    def __init__(self):
        self.request = UserRequest()
        self.payload = user_payload

    @allure.step("Получить список всех пользователей.")
    def step_get_users(self):
        """
        Получить список всех пользователей.

        :return: Объект Response.
        """
        response = self.request.get_users_request()
        CommonChecker.check_status_code_ok(response)
        return response


    @allure.step("Создать валидного пользователя.")
    def step_valid_user_create(self, **kwargs):
        """
        Создать валидного пользователя.

        :param kwargs: Параметры для конфигурации тела запроса.
        :return: Объект Response.
        """
        payload = self.payload.get_request_body_for_user(**kwargs)
        response = self.request.create_user_request(payload)
        # здесь будет коллектор
        CommonChecker.check_status_code_ok(response)
        return response


    @allure.step("Создать невалидного пользователя.")
    def step_invalid_user_create(self, **kwargs):
        """
        Создать невалидного пользователя.

        :param kwargs: Параметры для конфигурации тела запроса.
        :return: Объект Response.
        """
        payload = self.payload.get_request_body_for_user(**kwargs)
        response = self.request.create_user_request(payload)
        # здесь будет коллектор
        CommonChecker.check_status_code_422(response) # В теории можно вообще здесь не чекать статус код
        return response


    @allure.step("Получить пользователя по ID.")
    def step_get_user_by_id(self, user_id: int):
        """
        Получить пользователя по ID.

        :param user_id: ID пользователя.
        :return: Объект Response.
        """
        response = self.request.get_user_request(user_id)
        # здесь будет коллектор
        CommonChecker.check_status_code_ok(response)
        return response


    @allure.step("Обновить данные пользователя.")
    def step_update_user(self, user: dict, **kwargs):
        """
        Обновить данные пользователя по ID.
        :param user: Словарь с данными пользователя.
        :param kwargs: Параметры для конфигурации тела запроса.
        :return: Объект Response.
        """
        payload = self.payload.get_request_body_for_user_update(user, **kwargs)
        response = self.request.update_user_request(user.get("id"), payload)
        # здесь будет коллектор
        CommonChecker.check_status_code_ok(response)
        return response


    @allure.step("Удалить пользователя по ID.")
    def step_delete_user_by_id(self, user_id: int):
        """
        Удалить пользователя по ID.

        :param user_id: ID пользователя.
        :return: Объект Response.
        """
        response = self.request.delete_user_request(user_id)
        CommonChecker.check_status_code_ok(response)
        return response