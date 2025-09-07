class CommonChecker:
    """
    Класс содержащий общие чекеры.
    """
    @staticmethod
    def check_status_code(response, expected_status: int):
        """
        Проверка соответствия фактического статус-кода с ожидаемым.

        :param response: Объект Response.
        :param expected_status: Ожидаемый статус-код.
        """
        assert response.status_code == expected_status, (
            f"Ожидаемый статус-код: {expected_status}, фактический статус-код: {response.status_code}."
        )


    @staticmethod
    def check_key_exist(data: dict, key: str):
        """
        Проверка наличия ключа.

        :param data: Тело ответа.
        :param key: Ожидаемый ключ.
        """
        assert key in data, f"В ответе отсутствует обязательный ключ '{key}'."


    @staticmethod
    def check_value_data_type(data: dict, key: str, expected_data_type: type):
        """
        Проверка типа данных значения ключа.

        :param data: Тело ответа.
        :param key: Ожидаемый ключ.
        :param expected_data_type: Ожидаемый тип данных значения ключа.
        """
        value = data[key]
        assert isinstance(value, expected_data_type), (
            f"Ожидаемый тип данных значения: {expected_data_type}. "
            f"Фактический тип данных: {type(value)}. Значение: {value}."
        )


    @staticmethod
    def check_response_data_type(response, expected_data_type: type):
        """
        Проверка типа данных ответа от сервера.

        :param response: Объект Response.
        :param expected_data_type: Ожидаемый тип данных.
        """
        data = response.json()
        assert isinstance(data, expected_data_type), (
            f"Ожидаемый тип данных: {expected_data_type}, фактический тип данных: {type(data)}"
        )


    @staticmethod
    def check_equal_dicts(expected_dict: dict, actual_dict: dict):
        """
        Проверка соответствия ожидаемого тела ответа с фактическим.

        :param expected_dict: Ожидаемое тело ответа.
        :param actual_dict: Фактическое тело ответа.
        """
        assert expected_dict == actual_dict, (
            f"Ожидаемое тело ответа: {expected_dict}, фактическое тело ответа: {actual_dict}"
        )


    # Улучшить метод, не очевидно что с чем сравнивается, откуда берется и т.д.
    @staticmethod
    def check_equal_response_bodies(response1, response2):
        """
        Проверка соответствия одного тела ответа с другим телом ответа от сервера.

        :param response1: Объект Response.
        :param response2: Объект Response.
        """
        body1 = response1.json()
        body2 = response2.json()

        assert body1 == body2, (
            f"Тело ответа: {body2}, не совпадает с телом ответа: {body1}"
        )