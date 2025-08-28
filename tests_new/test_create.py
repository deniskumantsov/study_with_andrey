from steps.user_steps import UserSteps
from checkers.user_checker import CommandChecker
import pytest
from utils.generators import generate_valid_patronymic_none
from data import data_test_user as test_data


# Добавить проверку заголовков
def test_create_user_with_non_required(delete_user):
    """
    Позитивная проверка создания пользователя с отчеством.
    :param user_request:
    :return:
    """
    user_steps = UserSteps()
    # 1. Создать пользователя с валидными данными.
    user_data_response = user_steps.user_create_successful(**test_data.request_body)
    # 2. Проверить наличие созд пользователя в БД.
    user_data = user_steps.get_user_by_id(user_id=user_data_response["json"]["id"])
    CommandChecker.check_response_body(user_data, test_data.request_body)
    delete_user(user_data_response["json"]["id"])


# def test_create_user_with_patronymic(user_request):
#     """
#     Позитивная проверка создания пользователя с отчеством.
#     :param user_request:
#     :return:
#     """
#     payload = get_request_body_for_user()
#
#     create_response = user_request.create_user_request(payload)
#     print(create_response)
#     CommandChecker.check_status_code(create_response, 200)
#     CommandChecker.check_response_body(create_response, payload)
#
#     user_id = create_response["json"]["id"]
#     get_response = user_request.get_user_request(user_id)
#     print(get_response)
#     CommandChecker.check_status_code(get_response, 200)
#     CommandChecker.check_response_body(get_response, payload)
#
#     delete_response = user_request.delete_user_request(user_id)
#     print(delete_response)
#     CommandChecker.check_status_code(delete_response, 200)
#
#     get_response = user_request.get_user_request(user_id)
#     CommandChecker.check_status_code(get_response, 404)
#
#
#
# def test_create_user_without_non_requirement(user_request):
#     """
#     Позитивная проверка создания пользователя без отчества.
#     :param user_request:
#     :return:
#     """
#
#     payload = get_request_body_for_user()
#     payload["patronymic"] = generate_valid_patronymic_none()
#
#     create_response = user_request.create_user_request(payload)
#     print(create_response)
#     CommandChecker.check_status_code(create_response, 200)
#     CommandChecker.check_response_body(create_response, payload)
#
#     user_id = create_response["json"]["id"]
#     get_response = user_request.get_user_request(user_id)
#     print(get_response)
#     CommandChecker.check_status_code(get_response, 200)
#     CommandChecker.check_response_body(get_response, payload)
#
#     delete_response = user_request.delete_user_request(user_id)
#     print(delete_response)
#     CommandChecker.check_status_code(delete_response, 200)
#
#     get_response = user_request.get_user_request(user_id)
#     CommandChecker.check_status_code(get_response, 404)
