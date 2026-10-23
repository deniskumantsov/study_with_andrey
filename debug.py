from dataclasses import dataclass, field, asdict
from typing import Optional

# Пример реализации payload через dataclass
# @dataclass
# class UserResponseSchema:
#     """
#     Структура ответа сервера при работе с пользователем.
#     """
#     phone_number: int = field(default_factory=generate_valid_phone_number)
#     firstname: str = field(default_factory=generate_valid_firstname)
#     lastname: str = field(default_factory=generate_valid_lastname)
#     patronymic: Optional[str] = None
#     birthday: str = field(default_factory=generate_valid_birthday)
#     passport_serial: int = field(default_factory=generate_valid_passport_serial)
#     passport_number: int = field(default_factory=generate_valid_passport_number)
#     password: str = field(default_factory=generate_valid_password)
#
#     def as_payload(self):
#         if self.patronymic:
#             return asdict(self)
#         else:
#             payload = asdict(self)
#             del payload["patronymic"]
#             return payload
#
#
# if __name__ == "__main__":
#     payload = UserResponseSchema(phone_number="denis molodec")
#     payload.title="andrey molodec"
#     print(payload.title)
#     print(payload.as_payload())


# @staticmethod
# def check_equal_response_bodies(response1,
#                                 response2):  # Улучшить метод, не очевидно что с чем сравнивается, откуда берется и т.д.
#     """
#     Проверка соответствия одного тела ответа с другим телом ответа от сервера.
#
#     :param response1: Объект Response.
#     :param response2: Объект Response.
#     """
#     body1 = response1.json()
#     body2 = response2.json()
#
#     assert body1 == body2, (
#         f"Тело ответа: {body2}, не совпадает с телом ответа: {body1}"
#     )


# Как передать данные в Фикстуру?
# test_data = {"username": "Petya", "pass": "12345"}
#  @pytest.mark.parametrize("user(<-Это имя фикстуры)", [test_data], indirect=True)
#  def test_any(user):
#       .....
#       check......(user)
#       .....


# test_data_2 = ("Petya", "12345")
#  @pytest.mark.parametrize("username, pass(<-Это ссылки на данные)", [test_data_2])

# Как передать данные в Фикстуру?
# test_data = {"username": "Petya", "pass": "12345"}
#  @pytest.mark.parametrize("user(<-Это имя фикстуры)", [test_data], indirect=True)
#  def test_any(user):
#       .....
#       check......(user)
#       .....



# test_data_2 = ("Petya", "12345")
#  @pytest.mark.parametrize("username, pass(<-Это ссылки на данные)", [test_data_2])

# # 1. request.param
# @pytest.fixture()
# def user(request):
#     """
#     :param request:
#     :return:
#     """
#     user_data = request.param # request.param = {"username": "Petya", "pass": "12345"}/None
#     # Вставить проверку на то что в param у нас dict.
#     if isinstance(user_data, (dict, None)):
#         user_steps = UserSteps()
#         if user_data:
#             user = user_steps.step_user_create(expected_status=200, **user_data).json()
#         else:
#             user = user_steps.step_user_create(expected_status=200).json()
#
#         yield user
#         user_steps.step_delete_user_by_id(user.get("id"))
#         user_steps.step_get_user_by_id(user.get("id"), expected_status=404)
#     else:
#         pytest.fail("Ошибка! Проверить тестовые данные")
#
#
#
# 2. Через замыкание
@pytest.fixture
def user():

    def _user(user_data: dict):
        user_steps = UserSteps()
        if user_data:
            user = user_steps.step_user_create(expected_status=200, **user_data).json()
        else:
            user = user_steps.step_user_create(expected_status=200).json()
        collector.append(user)
    return _user

@pytest.fixture(scope=session, autouse=True)
def clear_collector():
    yield
    # Пост удаление всех созданнызх пользователей за тестовую сессию
    collector.clear()



test_data = {"username": "Petya", "pass": "12345"}
def test_any(user):
    user = user(test_data)
    .....
    check......(user)
    .....
#
# # 3. Через параметры фикстуры
#
# @pytest.fixture
# def user(username, password):
#
#     user_steps = UserSteps()
#     user = user_steps.step_user_create(expected_status=200, username=username, password=password).json()
#     yield user
#     user_data = uaer_steps.step_get_user_by_name(username)
#     user_steps.step_delete_user_by_id(user_data.get("id"))
#     user_steps.step_get_user_by_id(user_data.get("id"), expected_status=404)
#
#
#
# test_data_3 = ("Petya", "12345")
# @pytest.mark.parametrize("username, password(<-Это ссылки на данные(аля временные фикстуры))", [test_data_3])
# def test_any(user, username, password):
#     .....
#     check......(user)
#     .....

# ("P&ass1!'; DROP TABLE users; --", 422),
# ("P&ass1!<script>alert('xss')</script>", 422),
# ("P&ass1! OR 1=1", 422),








@allure.step("Создать пользователя.")
    def step_user_create(self, expected_status: int, **kwargs):
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


    @allure.step("Создать валидного пользователя.")
    def step_user_create_successful(self, **kwargs):
        """
        Создать валидного пользователя.

        :param kwargs: Параметры для конфигурации тела запроса.
        :return: Объект Response.
        """
        response = self.step_user_create(expected_status=200, **kwargs)
        payload = json.loads(response.request.body)
        UserChecker.check_response_body(response, payload)
        return response


    @allure.step("Создать невалидного пользователя.")
    def step_user_create_unsuccessful(self, **kwargs):
        """
        Создать невалидного пользователя.

        :param kwargs: Параметры для конфигурации тела запроса.
        :return: Объект Response.
        """
        payload = self.payload.get_request_body_for_user(**kwargs)
        response = self.request.create_user_request(payload)
        return response






@pytest.mark.parametrize("firstname, expected_status", test_data.firstname_test_data)
def test_create_user_with_invalid_firstname(firstname, expected_status, entity_collector):
    """
    Негативная проверка создания пользователя с невалидным именем.
    Шаги:
    1. Создать пользователя с невалидным firstname.
        - Отправить POST-запрос.
        - Проверить статус-код == expected_status.
    2. Удалить созданного пользователя.

    :param firstname: Имя пользователя.
    :param expected_status: Ожидаемый статус-код.
    :param entity_collector: Фикстура для удаления созданных сущностей.
    """
    user_steps = UserSteps()
    user_data_response = user_steps.step_user_create_unsuccessful(firstname=firstname, expected_status=expected_status)

    entity_collector(user_data_response)

    CommonChecker.check_status_code(user_data_response, expected_status)


@pytest.fixture()
def entity_collector():
    """
    Фикстура для сбора пользователей, созданных в тестах.

    - Если сервер неожиданно вернул 200 и создал пользователя, ID сохраняется.
    - После теста все собранные пользователи удаляются.
    """
    created_users = []

    def _collector(response):
        if response.status_code == 200:
            user_id = response.json().get("id")
            created_users.append(user_id)

    yield _collector

    user_steps = UserSteps()
    for user_id in created_users:
        user_steps.step_delete_user_by_id(user_id)
        user_steps.step_get_user_by_id(user_id, expected_status=404)



@pytest.fixture()
def user(request):
    """

    :param request:
    :return:
    """
    user_data = request.param
    user_steps = UserSteps()
    if user_data:
        user = user_steps.step_user_create(expected_status=200, **user_data).json()
    else:
        user = user_steps.step_user_create(expected_status=200).json()

    yield user
    user_steps.step_delete_user_by_id(user.get("id"))
    user_steps.step_get_user_by_id(user.get("id"), expected_status=404)




# С такой реализации придется создавать много экземпляров класса, это плохо. Либо сделать где то некий глобальный экземпляр класса.
# Но где он будет не понятно че-то.
# class Collector:
#
#     def __init__(self):
#         self.created_users = []
#
#
#     def add(self, user_id: int):
#         self.created_users.append(user_id)
#
#
#     def cleanup(self, user_steps):
#         for user_id in self.created_users:
#             user_steps.step_delete_user_by_id(user_id)
#         self.created_users.clear()






# user_info = namedtuple("UserShortInfo", ["id", "name", "notes"])

class DataCollector:
    _data_dict = defaultdict(list)

    def __init__(self):
        self.__dict__ = self._data_dict

    def collect(entity: dict):
        user_info = UserShortInfo(id=entity["id"], name=entity["firstname"], notes=None)
        self.self._data_dict.append(user_info)

    def update(entity_id: str, info: str = "deleted"):
        for entity in self.self._data_dict:
            if entity.id == entity_id:
                updated_entity = entity._replace(note=info)


collector = DataCollector()


# collector.__dict__()


def create_user()
    .....
    collector.collect({"entity_id": 123, "name": "Petya"})
    ....


@pytest.fixture
def clear_collector(scope=session, autouse=True):
    dc = DataCollector()
    dc._data_dict = [{..}, {...}, {..}, {...}]
    Чекаем все сущности у которых note != deleted и через for их удаляем











# phone_number_test_data = [
#     # Длина числа
#     (999999999, 422),
#     (10000000000, 422),
#     (-1, 422),
#     (0, 422),
#     (10**20, 422),
#
#
#     # Строки
#     ("8005553535", 422),
#     ("123", 422),
#     ("1234567890123", 422),
#     ("80055535аб", 422),
#     ("80055535!-", 422),
#     ("80055535@&", 422),
#
#     # Пробелы, табуляция, перенос строки
#     (" ", 422),
#     (" 8005553535", 422),
#     ("8005553535 ", 422),
#     ("800 5553535", 422),
#     ("\t8005553535", 422),
#     ("\n8005553535", 422),
#
#     # Пустая / None
#     ("", 422),
#     (None, 422),
#
#     # Булевы значения
#     (True, 422),
#     (False, 422),
#
#     # Списки и словари
#     ([], 422),
#     ({}, 422),
#
#     # Float
#     (3.14, 422),
# ]
#
# firstname_test_data = [
#     # Длина строки
#     ("а" * 1, 422),
#     # ("а" * 2, 200),
#     # ("а" * 3, 200),
#     # ("а" * 25, 200),
#     # ("а" * 254, 200),
#     # ("а" * 255, 200),
#     ("а" * 256, 422),
#     ("а" * 777, 422),
#
#     # Пустая / None
#     ("", 422),
#     (None, 422),
#
#     # Тип данных
#     (123, 422),
#     (3.14, 422),
#     (True, 422),
#     (False, 422),
#     (["Лика"], 422),
#     ({"Лика": "Денис"}, 422),
#
#     # Допустимые варианты с двойным именем
#     # ("Лика-Лика", 200),
#     # ("Лика Лика", 200),
#
#     # Латиница, цифры, символы, спецсимволы
#     ("Лика123", 422),
#     ("Лика!", 422),
#     ("Лика&", 422),
#     ("Denis", 422),
#     ("Denis123", 422),
#     ("Denis!", 422),
#     ("Denis&", 422),
#
#     # Пробелы, табуляция, перенос строки
#     (" ", 422),
#     (" Лика", 422),
#     ("Лика ", 422),
#     ("\tЛика", 422),
#     ("Лика\t", 422),
#     ("Ли\tка", 422),
#     ("\nЛика", 422),
#     ("Лика\n", 422),
#     ("Ли\nка", 422),
# ]
#
# lastname_test_data = [
#     # Длина строки
#     ("а" * 1, 422),
#     # ("а" * 2, 200),
#     # ("а" * 3, 200),
#     # ("а" * 25, 200),
#     # ("а" * 254, 200),
#     # ("а" * 255, 200),
#     ("а" * 256, 422),
#     ("а" * 777, 422),
#
#     # Пустая / None
#     ("", 422),
#     (None, 422),
#
#     # Тип данных
#     (123, 422),
#     (3.14, 422),
#     (True, 422),
#     (False, 422),
#     ([], 422),
#     ({}, 422),
#
#     # Допустимые варианты с двойной фамилией
#     # ("Петров-Сидоров", 200),
#     # ("Петров Сидоров", 200),
#
#     # Латиница, цифры, символы
#     ("Петров123", 422),
#     ("Петров!", 422),
#     ("Петров&", 422),
#     ("Petrov", 422),
#     ("Petrov123", 422),
#     ("Petrov!", 422),
#     ("Petrov&", 422),
#
#     # Пробелы, табуляция, перенос строки
#     (" ", 422),
#     (" Петров", 422),
#     ("Петров ", 422),
#     ("\tПетров", 422),
#     ("Петров\t", 422),
#     ("Пет\tров", 422),
#     ("\nПетров", 422),
#     ("Петров\n", 422),
#     ("Пет\nров", 422),
# ]
#
# patronymic_test_data = [
#     # Длина строки
#     ("а" * 1, 422),
#     # ("а" * 2, 200),
#     # ("а" * 3, 200),
#     # ("а" * 25, 200),
#     # ("а" * 254, 200),
#     # ("а" * 255, 200),
#     ("а" * 256, 422),
#     ("а" * 777, 422),
#
#     # Пустая / None
#     # ("", 200),
#     (None, 422),
#
#     # Тип данных
#     (123, 422),
#     (3.14, 422),
#     (True, 422),
#     (False, 422),
#     ([], 422),
#     ({}, 422),
#
#     # Латиница, цифры, символы
#     ("Игоревич123", 422),
#     ("Игоревич!", 422),
#     ("Игоревич&", 422),
#     ("Igor", 422),
#     ("Igor123", 422),
#     ("Igor!", 422),
#     ("Igor&", 422),
#
#     # Пробелы, табуляция, перенос строки
#     (" ", 422),
#     (" Игоревич", 422),
#     ("Иг ор", 422),
#     ("Игор ", 422),
#     ("\tИгоревич", 422),
#     ("Игоревич\t", 422),
#     ("И\tгор", 422),
#     ("\nИгоревич", 422),
#     ("Игоревич\n", 422),
#     ("И\nгор", 422),
# ]
#
# birthday_test_data = [
#     # Пустые / None
#     (None, 422),
#     ("", 422),
#
#     # (generate_birthday_age_yesterday(16), 200),   # исполнилось 16 вчера
#     # (generate_birthday_exact_age(16), 200),       # ровно 16 сегодня
#     (generate_birthday_age_tomorrow(16), 422),    # завтра 16
#     # (generate_birthday_exact_age(17), 200),       # 17 лет
#     (generate_birthday_exact_age(100), 422),      # 100 лет
#
#     ("1999-09-03!", 422),
#     ("1999-09-0!", 422),
#     ("1999-09-03&", 422),
#     ("1999-09-03ааа", 422),
#     ("1999-0ааа", 422),
#     ("1999.09.03", 422),
#     ("1999/09/03", 422),
#     ("1999&09&03", 422),
#     ("0000-00-00", 422),
#     ("2020-00-12", 422),
#     ("2021-12-00", 422),
#     ("0000-01-12", 422),
#     # ("1970-01-01", 200),
#     ("9999-99-99", 422),
#     ("9999-12-01", 422),
#     ("2000-99-01", 422),
#     ("2000-12-99", 422),
#     ("2000-02-31", 422),
#     ("2000-12-32", 422),
#     ("2099-12-12", 422),
#
#     # ("2008-02-29", 200),  # високосный год, ровно 17 лет
#     # ("2009-02-28", 200),  # 16 лет, 28 февраля
#     ("2009-02-29", 422),  # невисокосный год, 28 дней в месяце
#     # ("2008-04-30", 200),  # 30 апреля
#     # ("2008-03-31", 200),  # 31 марта
#     ("2008-04-31", 422),  # 31 апреля, в этом году 30 дней в апреле.
#
#     (" ", 422),
#     (" 1999-09-03", 422),
#     ("1999-09-03 ", 422),
#     ("1999- 09-03", 422),
#     ("\t1999-09-03", 422),
#     ("1999-09-03\t", 422),
#     ("1999-\t09-03", 422),
#     ("\n1999-09-03", 422),
#     ("1999-09-03\n", 422),
#     ("1999-\n09-03", 422),
#
#     # Тип данных
#     (123, 422),
#     (3.14, 422),
#     (True, 422),
#     (False, 422),
#     ([], 422),
#     ({}, 422),
# ]
#
# passport_serial_test_data = [
#     # Валидные данные
#     # ("0000", 200),
#     # ("1234", 200),
#     # ("9999", 200),
#
#     # Длина строки
#     ("1", 422),
#     ("12", 422),
#     ("123", 422),
#     ("12345", 422),
#     ("1" * 100, 422),
#
#     # Пустое / None
#     ("", 422),
#     (None, 422),
#
#     # Тип данных
#     (1234, 422),
#     (3.14, 422),
#     (True, 422),
#     (False, 422),
#     ([], 422),
#     ({}, 422),
#
#     ("123б", 422),
#     ("abcd", 422),
#     ("123!", 422),
#     ("123&", 422),
#     (" ", 422),
#     (" 123", 422),
#     ("123 ", 422),
#     ("12 3", 422),
#     ("\t1234", 422),
#     ("1234\t", 422),
#     ("12\t34", 422),
#     ("\n1234", 422),
#     ("1234\n", 422),
#     ("12\n34", 422),
#
#     # Граничные значения
#     # ("0001", 200),
#     # ("9998", 200),
#     ("10000", 422),
# ]
#
# passport_number_test_data = [
#     # Валидные данные
#     # ("000000", 200),
#     # ("123456", 200),
#     # ("999999", 200),
#
#     # Длина строки
#     ("1", 422),
#     ("12", 422),
#     ("123", 422),
#     ("1234", 422),
#     ("12345", 422),
#     ("1234567", 422),
#     ("1" * 100, 422),
#
#     # Пустое / None
#     ("", 422),
#     (None, 422),
#
#     # Тип данных
#     (123456, 422),
#     (3.14567, 422),
#     (True, 422),
#     (False, 422),
#     ([], 422),
#     ({}, 422),
#
#     # Нецифровые символы
#     ("12345б", 422),
#     ("12345!", 422),
#     ("12345&", 422),
#     ("1234ab", 422),
#     ("12$456", 422),
#     (" ", 422),
#     (" 12345", 422),
#     ("12345 ", 422),
#     ("12 345", 422),
#     ("\t123456", 422),
#     ("123456\t", 422),
#     ("12\t3456", 422),
#     ("\n123456", 422),
#     ("123456\n", 422),
#     ("12\n3456", 422),
#
#     # Граничные значения
#     # ("000001", 200),
#     # ("999998", 200),
#     ("1000000", 422),
# ]
#
# password_test_data = [
#     # Валидные пароли
#     # ("Password1!@", 200),
#     # ("A1b2C#3d4&", 200),
#     # ("Pass1@word.com", 200),
#     # ("PASSWORD1!", 200),
#
#     # Длина строки меньше 9
#     ("P1!", 422),
#     ("Pass1$", 422),
#     ("Abc1&", 422),
#     ("A1b2c3$", 422),
#     ("A1&" + "a" * 254, 422),
#     ("A1&" + "a" * 255, 422),
#     ("A1&" + "a" * 256, 422),
#     ("A1&" + "a" * 777, 422),
#
#     # Нет спецсимволов
#     ("Password1", 422),
#
#     # Нет цифр
#     ("Password", 422),
#
#     # Нет заглавных букв
#     ("password1&", 422),
#
#     # Кириллица
#     ("Пароль1!&", 422),
#
#     # Пустое / None
#     ("", 422),
#     (None, 422),
#
#     # Тип данных
#     (123456789, 422),
#     (3.14159265, 422),
#     (True, 422),
#     (False, 422),
#     ([], 422),
#     ({}, 422),
#
#     (" ", 422),
#     # (" A1b2c3d4&", 200),
#     # ("A1b2c3d4& ", 200),
#     # ("A1b2 c3d4&", 200),
#     ("\tA1b2c3d4&", 422),
#     ("A1b2c3d4&\t", 422),
#     ("A1b2c\t3d4&", 422),
#     ("\nA1b2c3d4&", 422),
#     ("A1b2c3d4&\n", 422),
#     ("A1b2\nc3d4&", 422),
#     ("\rA1b2c3d4&", 422),
#     ("A1b2c3d4&\r", 422),
#     ("\vA1b2c3d4&", 422),
#     ("A1b2c3d4&\v", 422),
#
#     ("P汉字sword1&!", 422),
#     ("Password1&!😊", 422),
#     ("Pässword1&!", 422),
#
#     # ("P&ass1!'; DROP TABLE users; --", 422),
#     # ("P&ass1!<script>alert('xss')</script>", 422),
#     # ("P&ass1! OR 1=1", 422),
# ]