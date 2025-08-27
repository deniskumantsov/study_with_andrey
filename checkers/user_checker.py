from schemas.user_response import UserResponse

# убрать return
class CommandChecker:
    """
    Класс для проверки ответа от сервера.
    """
    @staticmethod
    def check_status_code(response: dict, expected_status: int):
        """
        Проверка, что код ответа совпадает с ожидаемым.
        :param response: Словарь с ответом от сервера.
        :param expected_status: Ожидаемый код ответа.
        """
        assert response["status_code"] == expected_status, (
            f"Ожидаемый статус-код: {expected_status}, фактический статус-код: {response['status_code']}. "
            f"Тело ответа: {response['json']}"
        )


    @staticmethod
    def check_header_content_type(response: dict): # Переделать, проблема с регистром
        """
        Проверка, что заголовок ответа "Content-Type" есть, формат данных - "application/json".
        :param response: Словарь с ответом от сервера.
        :return:
        """
        assert response["headers"]["Content-Type"] == "application/json", (
            f"Ожидаемый формат данных: application/json, фактический формат данных: '{response['headers'].get('Content-Type')}'."
        )


    @staticmethod
    def check_response_body(response: dict, payload: dict):
        """
        Проверка, что данные в теле ответа совпадают с данными в теле запроса.
        :param response: Словарь с ответом от сервера.
        :param payload: Тело(json) запроса к серверу.
        :return:
        """
        user_response = UserResponse(**response["json"])
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