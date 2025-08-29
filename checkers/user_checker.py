from schemas.user_response import UserResponseSchema


class CommandChecker:
    """
    Класс для проверки ответа от сервера.
    """
    @staticmethod
    def check_status_code(response, expected_status: int):
        """
        Проверка, что код ответа совпадает с ожидаемым.
        :param response: Объект Response.
        :param expected_status: Ожидаемый статус код.
        """
        assert response.status_code == expected_status, (
            f"Ожидаемый статус-код: {expected_status}, фактический статус-код: {response.status_code}."
        )


    @staticmethod
    def check_response_body(response, payload: dict):
        """
        Проверка, что данные в теле ответа совпадают с ожидаемыми в теле ответа.
        :param response: Объект Response.
        :param payload: Тело запроса.
        """
        actual_response_body = response.json()
        expected_response_body = payload.copy()

        assert "id" in actual_response_body, "В теле ответа отсутствует обязательное поле 'id'."
        user_id = actual_response_body["id"]
        assert isinstance(user_id, int), f"Поле 'id' должно быть int, фактически: {type(user_id)}"

        actual_response_body.pop("id", None)
        expected_response_body.pop("password", None)
        assert actual_response_body == expected_response_body, (
            f"Ожидаемое тело ответа: {expected_response_body}, фактическое тело ответа: {actual_response_body}"
        )