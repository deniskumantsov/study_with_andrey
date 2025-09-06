import allure

from steps.user_steps import UserSteps
from checkers.user_checkers import UserChecker
from checkers.common_checkers import CommonChecker
import pytest
from data import data_test_user as test_data


def test_create_user_with_non_required(delete_user):
    """
    Позитивная проверка создания пользователя с отчеством.
    """
    user_steps = UserSteps()
    # 1. Создаем пользователя с валидными данными(отправляем POST-запрос).
    # - Проверяем статус-код.
    # - Проверяем payload(test_data.request_body_with_non_required без password) == телу ответа от сервера(без id).
    # - Проверяем что в ответе есть id(int).
    user_data_response = user_steps.user_create_successful(**test_data.request_body_with_non_required)

    # 2. Проверяем наличие созданного пользователя в БД(отправляем GET-запрос).
    # - Проверяем тело ответа(без id) == payload(test_data.request_body без password).
    # - Проверяем что в ответе есть id(int).
    user_data = user_steps.get_user_by_id(user_id=user_data_response.json()["id"])
    UserChecker.check_response_body(user_data, test_data.request_body_with_non_required)

    # 3. Удаляем созданного пользователя.
    delete_user(user_data_response.json()["id"])


def test_create_user_without_non_required(delete_user):
    """
    Позитивная проверка создания пользователя без отчества.

    :param delete_user:
    :return:
    """
    user_steps = UserSteps()
    # 1. Создаем пользователя с валидными данными(отправляем POST-запрос).
    # - Проверяем статус-код.
    # - Проверяем payload(test_data.request_body_without_non_required без password) == телу ответа от сервера(без id).
    # - Проверяем что в ответе есть id(int).
    user_data_response = user_steps.user_create_successful(**test_data.request_body_without_non_required)

    # 2. Проверяем наличие созданного пользователя в БД(отправляем GET-запрос).
    # - Проверяем тело ответа(без id) == payload(test_data.request_body_without_non_required без password).
    # - Проверяем что в ответе есть id(int).
    user_data = user_steps.get_user_by_id(user_id=user_data_response.json()["id"])
    UserChecker.check_response_body(user_data, test_data.request_body_without_non_required)

    # 3. Удаляем созданного пользователя.
    delete_user(user_data_response.json()["id"])


@pytest.mark.parametrize("phone_number, expected_status", test_data.phone_number_test_data)
def test_create_user_with_invalid_phone_number(phone_number, expected_status, entity_collector):
    """
    Негативная проверка создания пользователя с невалидным номером телефона.

    :param phone_number:
    :param expected_status:
    :param entity_collector:
    :return:
    """
    user_steps = UserSteps()
    user_data_response = user_steps.user_create(phone_number=phone_number, expected_status=expected_status)
    entity_collector(user_data_response)

# Подумать над доработкой
def test_register_user_with_non_unique_phone_number(delete_user):
    """
    Негативная проверка создания пользователя с неуникальным номером телефона.

    :param delete_user:
    :return:
    """
    user_steps = UserSteps()
    user_data_response = user_steps.user_create_successful(**test_data.request_body_with_non_required)
    user_id = user_data_response.json()["id"]
    user_steps.user_create(phone_number=test_data.request_body_with_non_required["phone_number"], expected_status=422)
    delete_user(user_id)


@pytest.mark.parametrize("firstname, expected_status", test_data.firstname_test_data)
def test_create_user_with_invalid_firstname(firstname, expected_status, entity_collector):
    """
    Негативная проверка создания пользователя с невалидным именем.

    :param firstname:
    :param expected_status:
    :param entity_collector:
    :return:
    """
    user_steps = UserSteps()
    user_data_response = user_steps.user_create(firstname=firstname, expected_status=expected_status)
    entity_collector(user_data_response)

@allure.title("Тест такой то")
@allure.feature("фича регистрации")
@pytest.mark.parametrize("lastname, expected_status", test_data.lastname_test_data)
def test_create_user_with_invalid_lastname(lastname, expected_status, entity_collector):
    """

    """
    user_steps = UserSteps()
    user_data_response = user_steps.user_create(lastname=lastname, expected_status=expected_status)
    entity_collector(user_data_response)


@pytest.mark.parametrize("patronymic, expected_status", test_data.patronymic_test_data)
def test_create_user_with_invalid_patronymic(patronymic, expected_status, entity_collector):
    """

    """
    user_steps = UserSteps()
    user_data_response = user_steps.user_create(patronymic=patronymic, expected_status=expected_status)
    entity_collector(user_data_response)



@pytest.mark.parametrize("birthday, expected_status", test_data.birthday_test_data)
def test_create_user_with_invalid_birthday(birthday, expected_status, entity_collector):
    """

    """
    user_steps = UserSteps()
    user_data_response = user_steps.user_create(birthday=birthday, expected_status=expected_status)
    entity_collector(user_data_response)


@pytest.mark.parametrize("passport_serial, expected_status", test_data.passport_serial_test_data)
def test_create_user_with_invalid_passport_serial(passport_serial, expected_status, entity_collector):
    """

    """
    user_steps = UserSteps()
    user_data_response = user_steps.user_create(passport_serial=passport_serial, expected_status=expected_status)
    entity_collector(user_data_response)


@pytest.mark.parametrize("passport_number, expected_status", test_data.passport_number_test_data)
def test_create_user_with_invalid_passport_number(passport_number, expected_status, entity_collector):
    """

    """
    user_steps = UserSteps()
    user_data_response = user_steps.user_create(passport_number=passport_number, expected_status=expected_status)
    entity_collector(user_data_response)


@pytest.mark.parametrize("password, expected_status", test_data.password_test_data)
def test_create_user_with_invalid_password(password, expected_status, entity_collector):
    """

    """
    user_steps = UserSteps()
    user_data_response = user_steps.user_create(password=password, expected_status=expected_status)
    entity_collector(user_data_response)


def test_get_users_list():
    """

    """
    user_steps = UserSteps()
    user_steps.get_users()




user_test_data = {"firstname": "Petya"}
# исправить, переделать
@pytest.mark.parametrize("user", [user_test_data], indirect=True)
def test_update_user(user):
    """

    """
    user_steps = UserSteps()

    # PATCH
    update_user_data = user_steps.update_user(
        user,
        firstname="NewFirst",
        lastname="NewLast",
        patronymic="NewPatr",
        birthday="1990-01-01",
        password="NewPass123&"
    )

    user_data = user_steps.get_user_by_id(update_user_data.json()["id"])

    CommonChecker.check_equal_response_bodies(update_user_data, user_data)
