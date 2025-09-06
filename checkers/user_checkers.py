import copy


class UserChecker:
    """
    Класс содержащий чекеры.
    """
    @staticmethod
    def check_response_body(response, payload: dict):
        """
        Проверка созданного пользователя. Ожидаемое тело ответа от сервера совпадает с payload.
        В теле ответ есть id.
        :param response: Объект Response.
        :param payload: Payload(dict).
        """
        actual_response_body = response.json()
        expected_response_body = copy.deepcopy(payload)

        assert "id" in actual_response_body, "В теле ответа отсутствует обязательное поле 'id'."
        user_id = actual_response_body["id"]
        assert isinstance(user_id, int), f"Поле 'id' должно быть int, фактически: {type(user_id)}"

        actual_response_body.pop("id")
        expected_response_body.pop("password")
        assert actual_response_body == expected_response_body, (
            f"Ожидаемое тело ответа: {expected_response_body}, фактическое тело ответа: {actual_response_body}"
        )

    # Переместить подобное добро в CommonChecker
    @staticmethod
    def check_response_data_type(response):
        """
        Проверка типа данных ответа от сервера.
        :param response: Объект Response.
        """
        users = response.json()
        assert isinstance(users, list), (
            f"Ожидаемый тип данных в теле ответа list, фактический тип данных: {type(users)}"
        )

    # Переделать, цикл так себе написал и в целом метод так себе. id не канает, это не id пользователя.
    # Убрать enumerate и id, сделать for user in users
    @staticmethod
    def check_response_structure(response):
        """
        Проверка структуры пользователя.
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

        for id, user in enumerate(users):
            missing_keys = expected_keys - user.keys()
            assert not missing_keys, (
                f"В теле ответа у пользователя с id {user.get(id)} отсутствуют ключи: {missing_keys}"
            )