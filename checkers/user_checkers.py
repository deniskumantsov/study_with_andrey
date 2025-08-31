import copy


class UserChecker:
    """
    Класс содержащий проверки ответа от сервера.
    """
    @staticmethod
    def check_response_body(response, payload: dict):
        """
        Проверка создания нового пользователя. Ожидаемое тело ответа от сервера совпадает с payload.
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