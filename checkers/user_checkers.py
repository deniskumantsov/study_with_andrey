import copy
from checkers.common_checkers import CommonChecker


class UserChecker:
    """
    Класс содержащий чекеры для модуля user.
    """
    @staticmethod
    def check_response_body(response, payload: dict):
        """
        Проверка тела ответа при создании пользователя.
        Проверка соответствия ожидаемого тела ответа и фактического тела ответа.
        ID есть в теле ответа, тип данных ID - int.

        :param response: Объект Response.
        :param payload: Тело запроса.
        """
        actual_response_body = response.json()
        expected_response_body = copy.deepcopy(payload)

        CommonChecker.check_key_exist(actual_response_body, "id")
        CommonChecker.check_value_data_type(actual_response_body, "id", int)

        actual_response_body.pop("id")
        expected_response_body.pop("password")

        CommonChecker.check_equal_dicts(expected_response_body, actual_response_body)


    @staticmethod
    def check_response_structure(response):
        """
        Проверка структуры списка всех пользователей.
        Проверка, что все пользователи содержат обязательные ключи.

        :param response: Объект Response.
        """
        users = response.json()
        expected_keys = {
            "phone_number",
            "firstname",
            "lastname",
            "patronymic",
            "birthday",
            "passport_serial",
            "passport_number",
            "id",
        }

        for user in users:
            missing_keys = expected_keys - set(user.keys())
            assert not missing_keys, (
                f"У пользователя с id:{user.get('id')} отсутствуют ключи: {missing_keys}"
            )