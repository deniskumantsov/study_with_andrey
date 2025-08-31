class CommonChecker:
    """
    Класс содержащий проверки ответа от сервера.
    """
    @staticmethod
    def check_status_code(response, expected_status: int):
        """
        Проверка совпадения фактического статус-кода с ожидаемым.
        :param response: Объект Response.
        :param expected_status: Ожидаемый статус-код.
        """
        assert response.status_code == expected_status, (
            f"Ожидаемый статус-код: {expected_status}, фактический статус-код: {response.status_code}."
        )


    @staticmethod
    def check_equal_response_bodies(response1, response2):
        """
        Проверка совпадения одного тела ответа с другим телом ответа от сервера.
        :param response1: Объект Response.
        :param response2: Объект Response.
        """
        body1 = response1.json()
        body2 = response2.json()

        assert body1 == body2, (
            f"Тело ответа: {body2}, не совпадает с телом ответа: {body1}"
        )