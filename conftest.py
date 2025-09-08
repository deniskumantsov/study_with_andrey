from typing import Optional
import pytest
from endpoints.user_request import UserRequest
from steps.user_steps import UserSteps
from data import data_test_user as test_data


@pytest.fixture()
def create_and_delete_user(): # Можно сделать такую фикстуру где и setup и teardown. Или сделать две отдельных.
    """
    Фикстура для создания пользователя перед тестом и удаления после.
    Возвращает объект Response.
    """
    user_steps = UserSteps()
    user_data = user_steps.step_user_create_successful(**test_data.request_body_with_non_required)
    yield user_data

    user_steps.step_delete_user_by_id(user_data.json()["id"])
    user_steps.step_get_user_by_id(user_data.json()["id"], expected_status=404)


@pytest.fixture()
def create_user_response():
    """
    Фикстура для создания пользователя.
    Возвращает объект Response.
    """
    user_steps = UserSteps()
    response = user_steps.step_user_create_successful(**test_data.request_body_with_non_required)
    return response


@pytest.fixture()
def delete_user():
    """
    Фикстура для удаления пользователя по ID после теста.
    Возвращает функцию в тест.
    """
    user_steps = UserSteps()

    def _delete_user(user_id: int):
        """
        """
        user_steps.step_delete_user_by_id(user_id)
        user_steps.step_get_user_by_id(user_id, expected_status=404)

    return _delete_user


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