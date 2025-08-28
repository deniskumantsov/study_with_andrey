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
        :param payload: Тело(json) запроса к серверу.
        """
        user_response = UserResponseSchema(**response.json())
        assert user_response.phone_number == payload["phone_number"], (
            f"Ожидаемый phone_number: {payload['phone_number']}, фактический phone_number: {user_response.phone_number}"
        )
        assert user_response.firstname == payload["firstname"], (
            f"Ожидаемый firstname: {payload['firstname']}, фактический firstname: {user_response.firstname}"
        )
        assert user_response.lastname == payload["lastname"], (
            f"Ожидаемый lastname: {payload['lastname']}, фактический lastname: {user_response.lastname}"
        )
        assert user_response.patronymic == payload["patronymic"], (
            f"Ожидаемый patronymic: {payload['patronymic']}, фактический patronymic: {user_response.patronymic}"
        )
        assert user_response.birthday == payload["birthday"], (
            f"Ожидаемый birthday: {payload['birthday']}, фактический birthday: {user_response.birthday}"
        )
        assert user_response.passport_serial == payload["passport_serial"], (
            f"Ожидаемый passport_serial: {payload['passport_serial']}, фактический passport_serial: {user_response.passport_serial}"
        )
        assert user_response.passport_number == payload["passport_number"], (
            f"Ожидаемый passport_number: {payload['passport_number']}, фактический passport_number: {user_response.passport_number}"
        )


    # @staticmethod
    # def check_header_content_type(response: dict): # Переделать, проблема с регистром
    #     """
    #     Проверка, что заголовок ответа "Content-Type" есть, формат данных - "application/json".
    #     :param response: Словарь с ответом от сервера.
    #     """
    #     assert response["headers"]["Content-Type"] == "application/json", (
    #         f"Ожидаемый формат данных: application/json, фактический формат данных: '{response['headers'].get('Content-Type')}'."
    #     )
    #
