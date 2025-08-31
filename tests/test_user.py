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


@pytest.mark.parametrize("invalid_phone", test_data.invalid_phone_numbers)
def test_create_user_with_invalid_phone_number(invalid_phone):
    """

    """
    user_steps = UserSteps()
    user_steps.user_create_with_expected_failure(phone_number=invalid_phone)


def test_register_user_with_non_unique_phone_number(delete_user):
    """

    """
    user_steps = UserSteps()
    user_data_response = user_steps.user_create_successful(**test_data.request_body_with_non_required)
    user_id = user_data_response.json()["id"]
    user_steps.user_create_with_expected_failure(phone_number=test_data.request_body_with_non_required["phone_number"])
    delete_user(user_id)


@pytest.mark.parametrize("firstname, expected_status", test_data.invalid_firstnames)
def test_create_user_with_invalid_firstnames(firstname, expected_status):
    """

    """
    user_steps = UserSteps()
    user_steps.user_create_with_expected_failure(firstname=firstname, expected_status=expected_status)
