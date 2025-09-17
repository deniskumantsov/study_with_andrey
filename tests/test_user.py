import allure
import pytest
from steps.user_steps import UserSteps
from checkers.user_checkers import UserChecker
from checkers.common_checkers import CommonChecker
from data import data_test_user as test_data

# хуета полная, молодец. Проверить что в респонсе есть тот пользак котоырй создан в фикстуре
@pytest.mark.parametrize("user", ["random"], indirect=True)
def test_get_users_list(user):
    """
    Позитивная проверка получения списка всех пользователей.
    Шаги:
    1. Создать пользователя с валидными данными.
    2. Получить список всех пользователей.
        - Отправить GET-запрос.
        - Проверить статус-код == 200.
    3. Проверить структуру ответа.
        - Тип данных ответа.
        - Структура пользователя.
    4. Проверить что созданный пользователь есть в списке.
    5. Удалить созданного пользователя.

    :param user:
    """
    user_steps = UserSteps()

    # Получить список всех пользователей
    users_data_response = user_steps.step_get_users()

    # Проверка типа данных ответа
    CommonChecker.check_response_data_type(users_data_response, list)

    # Проверка структуры пользователей
    UserChecker.check_response_structure(users_data_response)

    # Проверка, что созданный пользователь есть в списке
    UserChecker.check_user_in_list(users_data_response, user)


def test_create_user_with_non_required(delete_user):
    """
    Позитивная проверка создания пользователя с необязательным полем.
    Шаги:
    1. Создать пользователя с валидными данными, с необязательным полем patronymic.
        - Отправить POST-запрос.
        - Проверить статус-код == 200.
        - Проверить тело ответа. Payload == тело ответа.
        - В теле ответа есть ID, тип данных int.
    2. Проверить наличие созданного пользователя в БД.
        - Отправить GET-запрос.
        - Проверить тело ответа. Тело ответа POST-запроса == телу ответа GET-запроса.
    3. Удалить созданного пользователя.

    :param delete_user:
    """
    user_steps = UserSteps()
    user_data_response = user_steps.step_valid_user_create(**test_data.request_body_with_non_required)
    UserChecker.check_response_body(user_data_response, test_data.request_body_with_non_required)

    user_id = user_data_response.json()["id"]

    user_data = user_steps.step_get_user_by_id(user_id=user_id)
    CommonChecker.check_equal_response_bodies(user_data_response, user_data)

    delete_user(user_id)


def test_create_user_without_non_required(delete_user):
    """
    Позитивная проверка создания пользователя без необязательного поля.
    Шаги:
    1. Создать пользователя с валидными данными, без необязательного поля patronymic.
        - Отправить POST-запрос.
        - Проверить статус-код == 200.
        - Проверить тело ответа. Payload == тело ответа.
        - В теле ответа есть ID, тип данных int.
    2. Проверить наличие созданного пользователя в БД.
        - Отправить GET-запрос.
        - Проверить тело ответа. Тело ответа POST-запроса == телу ответа GET-запроса.
    3. Удалить созданного пользователя.

    :param delete_user:
    """
    user_steps = UserSteps()
    user_data_response = user_steps.step_valid_user_create(**test_data.request_body_without_non_required)
    UserChecker.check_response_body(user_data_response, test_data.request_body_without_non_required)

    user_id = user_data_response.json()["id"]

    user_data = user_steps.step_get_user_by_id(user_id=user_id)
    CommonChecker.check_equal_response_bodies(user_data_response, user_data)

    delete_user(user_id)


def test_register_user_with_non_unique_phone_number(delete_user): # Подумать над доработкой
    """
    Негативная проверка создания пользователя с неуникальным номером телефона.
    Шаги:
    1. Создать пользователя с валидными данными (POST-запрос).
        - Проверить статус-код == 200.
        - Проверить тело ответа (payload == тело ответа).
    2. Создать второго пользователя с тем же номером телефона.
        - Отправить POST-запрос.
        - Проверить статус-код == 422.
    3. Удалить созданного пользователя.

    :param delete_user:
    """
    user_steps = UserSteps()
    user_data_response = user_steps.step_valid_user_create(**test_data.request_body_with_non_required)
    UserChecker.check_response_body(user_data_response, test_data.request_body_with_non_required)

    user_id = user_data_response.json()["id"]

    user_steps.step_invalid_user_create(phone_number=test_data.request_body_with_non_required["phone_number"])

    delete_user(user_id)


@pytest.mark.parametrize("phone_number", test_data.negative_phone_number_test_data)
def test_create_user_with_invalid_phone_number(phone_number):
    """
    Негативная проверка создания пользователя с невалидным номером телефона.
    Шаги:
    1. Создать пользователя с невалидным phone_number.
        - Отправить POST-запрос.
        - Проверить статус-код.

    :param phone_number: Номер телефона.
    """
    user_steps = UserSteps()
    user_steps.step_invalid_user_create(phone_number=phone_number)


@pytest.mark.parametrize("firstname", test_data.negative_firstname_test_data)
def test_create_user_with_invalid_firstname(firstname):
    """
    Негативная проверка создания пользователя с невалидным именем.
    Шаги:
    1. Создать пользователя с невалидным firstname.
        - Отправить POST-запрос.
        - Проверить статус-код.

    :param firstname: Имя пользователя.
    """
    user_steps = UserSteps()
    user_steps.step_invalid_user_create(firstname=firstname)


@allure.title("Тест создания пользователя с невалидной фамилией.")
@allure.feature("Фича регистрации нового пользователя.")
@pytest.mark.parametrize("lastname", test_data.negative_lastname_test_data)
def test_create_user_with_invalid_lastname(lastname):
    """
    Негативная проверка создания пользователя с невалидной фамилией.
    Шаги:
    1. Создать пользователя с невалидным lastname.
        - Отправить POST-запрос.
        - Проверить статус-код.

    :param lastname: Фамилия пользователя.
    """
    user_steps = UserSteps()
    user_steps.step_invalid_user_create(lastname=lastname)


@pytest.mark.parametrize("patronymic", test_data.negative_patronymic_test_data)
def test_create_user_with_invalid_patronymic(patronymic):
    """
    Негативная проверка создания пользователя с невалидным отчеством.
    Шаги:
    1. Создать пользователя с невалидным patronymic.
        - Отправить POST-запрос.
        - Проверить статус-код.

    :param patronymic: Отчество пользователя.
    """
    user_steps = UserSteps()
    user_steps.step_invalid_user_create(patronymic=patronymic)


@pytest.mark.parametrize("birthday", test_data.negative_birthday_test_data)
def test_create_user_with_invalid_birthday(birthday):
    """
    Негативная проверка создания пользователя с невалидной датой рождения.
    Шаги:
    1. Создать пользователя с невалидным birthday.
        - Отправить POST-запрос.
        - Проверить статус-код.

    :param birthday: Дата рождения пользователя.
    """
    user_steps = UserSteps()
    user_steps.step_invalid_user_create(birthday=birthday)


@pytest.mark.parametrize("passport_serial", test_data.negative_passport_serial_test_data)
def test_create_user_with_invalid_passport_serial(passport_serial):
    """
    Негативная проверка создания пользователя с невалидной серией паспорта.
    Шаги:
    1. Создать пользователя с невалидным passport_serial.
        - Отправить POST-запрос.
        - Проверить статус-код.

    :param passport_serial: Серия паспорта пользователя.
    """
    user_steps = UserSteps()
    user_steps.step_invalid_user_create(passport_serial=passport_serial)


@pytest.mark.parametrize("passport_number", test_data.negative_passport_number_test_data)
def test_create_user_with_invalid_passport_number(passport_number):
    """
    Негативная проверка создания пользователя с невалидным номером паспорта.
    Шаги:
    1. Создать пользователя с невалидным passport_number.
        - Отправить POST-запрос.
        - Проверить статус-код.

    :param passport_number: Номер паспорта пользователя.
    """
    user_steps = UserSteps()
    user_steps.step_invalid_user_create(passport_number=passport_number)


@pytest.mark.parametrize("password", test_data.negative_password_test_data)
def test_create_user_with_invalid_password(password):
    """
    Негативная проверка создания пользователя с невалидным паролем.
    Шаги:
    1. Создать пользователя с невалидным password.
        - Отправить POST-запрос.
        - Проверить статус-код.

    :param password: Пароль пользователя.
    """
    user_steps = UserSteps()
    user_steps.step_invalid_user_create(password=password)


@pytest.mark.parametrize("user", ["random"], indirect=True)
def test_get_user_by_valid_id(user):
    """
    Позитивная проверка получения пользователя по ID.
    Шаги:
    1. Создать пользователя.
    2. Получить пользователя по его ID.
        - Отправить GET-запрос.
        - Проверить статус-код.
        - Проверить тело ответа, полученное при GET-запросе по ID.
    3. Удалить созданного пользователя.

    :param user:
    """
    user_steps = UserSteps()
    user_id = user.get("id")

    user_data_response = user_steps.step_get_user_by_id(user_id=user_id)

    user_data = user_data_response.json()
    CommonChecker.check_equal_dicts(user, user_data)


@pytest.mark.parametrize("user", ["random"], indirect=True)
def test_get_user_by_invalid_id(user):
    """
    Негативная проверка получения пользователя по ID.
    Шаги:
    1. Создать пользователя.
    2. Удалить пользователя.
    3. Отправить GET-запрос по не существующему ID удаленного пользователя.

    :param user:
    """
    user_steps = UserSteps()
    user_id = user.get("id")

    # Удаляем пользователя через шаг
    user_steps.step_delete_user_by_id(user_id)

    # GET по удалённому ID
    user_steps.step_get_user_by_id(user_id=user_id, expected_status=422)



@pytest.mark.parametrize("user", ["random"], indirect=True)
def test_update_user(user): # Разобраться
    """

    """
    user_steps = UserSteps()

    # PATCH
    update_user_data = user_steps.step_update_user(
        user,
        firstname="NewFirst",
        lastname="NewLast",
        patronymic="NewPatr",
        birthday="1990-01-01",
        password="NewPass123&"
    )

    user_data = user_steps.step_get_user_by_id(update_user_data.json()["id"])

    CommonChecker.check_equal_response_bodies(update_user_data, user_data)



