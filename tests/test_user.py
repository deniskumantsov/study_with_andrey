import allure
import pytest
from steps.user_steps import UserSteps
from checkers.user_checkers import UserChecker
from checkers.common_checkers import CommonChecker
from data import data_test_user as test_data


def test_get_users_list(create_and_delete_user):
    """
    Позитивная проверка получения списка всех пользователей.
    Шаги:
    1. Создать пользователя с валидными данными.
    2. Получить список всех пользователей.
        - Отправить GET-запрос
        - Проверить статус-код == 200.
    3. Проверить структуру ответа.
        - Тип данных ответа.
        - Структура пользователя.
    4. Удалить созданного пользователя.

    :param create_and_delete_user:
    """
    user_steps = UserSteps()
    user_data_response = user_steps.step_get_users()

    CommonChecker.check_response_data_type(user_data_response, list)
    UserChecker.check_response_structure(user_data_response)


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
    user_data_response = user_steps.step_user_create_successful(**test_data.request_body_with_non_required)

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
    user_data_response = user_steps.step_user_create_successful(**test_data.request_body_without_non_required)

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
    user_data_response = user_steps.step_user_create_successful(**test_data.request_body_with_non_required)

    user_id = user_data_response.json()["id"]

    user_steps.step_user_create(phone_number=test_data.request_body_with_non_required["phone_number"], expected_status=422)

    delete_user(user_id)


@pytest.mark.parametrize("phone_number, expected_status", test_data.phone_number_test_data)
def test_create_user_with_invalid_phone_number(phone_number, expected_status, entity_collector):
    """
    Негативная проверка создания пользователя с невалидным номером телефона.
    Шаги:
    1. Создать пользователя с невалидным phone_number.
        - Отправить POST-запрос.
        - Проверить статус-код == expected_status.
    2. Удалить созданного пользователя.

    :param phone_number: Номер телефона.
    :param expected_status: Ожидаемый статус-код.
    :param entity_collector: Фикстура для удаления созданных сущностей.
    """
    user_steps = UserSteps()
    user_data_response = user_steps.step_user_create_unsuccessful(phone_number=phone_number, expected_status=expected_status)

    entity_collector(user_data_response)

    CommonChecker.check_status_code(user_data_response, expected_status)


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


@allure.title("Тест такой то")
@allure.feature("фича регистрации")
@pytest.mark.parametrize("lastname, expected_status", test_data.lastname_test_data)
def test_create_user_with_invalid_lastname(lastname, expected_status, entity_collector):
    """
    Негативная проверка создания пользователя с невалидной фамилией.
    Шаги:
    1. Создать пользователя с невалидным lastname.
        - Отправить POST-запрос.
        - Проверить статус-код == expected_status.
    2. Удалить созданного пользователя.

    :param lastname: Фамилия пользователя.
    :param expected_status: Ожидаемый статус-код.
    :param entity_collector: Фикстура для удаления созданных сущностей.
    """
    user_steps = UserSteps()
    user_data_response = user_steps.step_user_create_unsuccessful(lastname=lastname, expected_status=expected_status)

    entity_collector(user_data_response)

    CommonChecker.check_status_code(user_data_response, expected_status)


@pytest.mark.parametrize("patronymic, expected_status", test_data.patronymic_test_data)
def test_create_user_with_invalid_patronymic(patronymic, expected_status, entity_collector):
    """
    Негативная проверка создания пользователя с невалидным отчеством.
    Шаги:
    1. Создать пользователя с невалидным patronymic.
        - Отправить POST-запрос.
        - Проверить статус-код == expected_status.
    2. Удалить созданного пользователя.

    :param patronymic: Отчество пользователя.
    :param expected_status: Ожидаемый статус-код.
    :param entity_collector: Фикстура для удаления созданных сущностей.
    """
    user_steps = UserSteps()
    user_data_response = user_steps.step_user_create_unsuccessful(patronymic=patronymic, expected_status=expected_status)

    entity_collector(user_data_response)

    CommonChecker.check_status_code(user_data_response, expected_status)


@pytest.mark.parametrize("birthday, expected_status", test_data.birthday_test_data)
def test_create_user_with_invalid_birthday(birthday, expected_status, entity_collector):
    """
    Негативная проверка создания пользователя с невалидной датой рождения.
    Шаги:
    1. Создать пользователя с невалидным birthday.
        - Отправить POST-запрос.
        - Проверить статус-код == expected_status.
    2. Удалить созданного пользователя.

    :param birthday: Дата рождения пользователя.
    :param expected_status: Ожидаемый статус-код.
    :param entity_collector: Фикстура для удаления созданных сущностей.
    """
    user_steps = UserSteps()
    user_data_response = user_steps.step_user_create_unsuccessful(birthday=birthday, expected_status=expected_status)

    entity_collector(user_data_response)

    CommonChecker.check_status_code(user_data_response, expected_status)


@pytest.mark.parametrize("passport_serial, expected_status", test_data.passport_serial_test_data)
def test_create_user_with_invalid_passport_serial(passport_serial, expected_status, entity_collector):
    """
    Негативная проверка создания пользователя с невалидной серией паспорта.
    Шаги:
    1. Создать пользователя с невалидным passport_serial.
        - Отправить POST-запрос.
        - Проверить статус-код == expected_status.
    2. Удалить созданного пользователя.

    :param passport_serial: Серия паспорта пользователя.
    :param expected_status: Ожидаемый статус-код.
    :param entity_collector: Фикстура удаления созданных сущностей.
    """
    user_steps = UserSteps()
    user_data_response = user_steps.step_user_create_unsuccessful(passport_serial=passport_serial, expected_status=expected_status)

    entity_collector(user_data_response)

    CommonChecker.check_status_code(user_data_response, expected_status)


@pytest.mark.parametrize("passport_number, expected_status", test_data.passport_number_test_data)
def test_create_user_with_invalid_passport_number(passport_number, expected_status, entity_collector):
    """
    Негативная проверка создания пользователя с невалидным номером паспорта.
    Шаги:
    1. Создать пользователя с невалидным passport_number.
        - Отправить POST-запрос.
        - Проверить статус-код == expected_status.
    2. Удалить созданного пользователя.

    :param passport_number: Номер паспорта пользователя.
    :param expected_status: Ожидаемый статус-код.
    :param entity_collector: Фикстура для удаления созданных сущностей.
    """
    user_steps = UserSteps()
    user_data_response = user_steps.step_user_create_unsuccessful(passport_number=passport_number, expected_status=expected_status)

    entity_collector(user_data_response)

    CommonChecker.check_status_code(user_data_response, expected_status)


@pytest.mark.parametrize("password, expected_status", test_data.password_test_data)
def test_create_user_with_invalid_password(password, expected_status, entity_collector):
    """
    Негативная проверка создания пользователя с невалидным паролем.
    Шаги:
    1. Создать пользователя с невалидным password.
        - Отправить POST-запрос.
        - Проверить статус-код == expected_status.
    2. Удалить созданного пользователя.

    :param password: Пароль пользователя.
    :param expected_status: Ожидаемый статус-код.
    :param entity_collector: Фикстура для удаления созданных сущностей.
    """
    user_steps = UserSteps()
    user_data_response = user_steps.step_user_create_unsuccessful(password=password, expected_status=expected_status)

    entity_collector(user_data_response)

    CommonChecker.check_status_code(user_data_response, expected_status)


def test_get_user_by_valid_id(create_and_delete_user):
    """
    Позитивная проверка получения пользователя по ID.
    Шаги:
    1. Создать пользователя.
    2. Получить пользователя по его ID.
        - Отправить GET-запрос.
        - Проверить статус-код.
        - Проверить тело ответа, полученное при GET-запросе по ID.
    3. Удалить созданного пользователя.

    :param create_and_delete_user:
    """
    user_steps = UserSteps()
    user_id = create_and_delete_user.json()["id"]

    user_data_response = user_steps.step_get_user_by_id(user_id=user_id)

    CommonChecker.check_equal_response_bodies(create_and_delete_user, user_data_response)


def test_get_user_by_invalid_id(create_user_response, delete_user):
    """
    Негативная проверка получения пользователя по ID.

    :param create_user_response:
    :param delete_user:
    :return:
    """
    user_steps = UserSteps()
    user_id = create_user_response.json()["id"]

    # Удаляем пользователя через фикстуру
    delete_user(user_id)

    # GET по несущ ID
    user_steps.step_get_user_by_id(user_id=user_id, expected_status=422)


user_test_data = {"firstname": "Petya"}
@pytest.mark.parametrize("user", [user_test_data], indirect=True)
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
