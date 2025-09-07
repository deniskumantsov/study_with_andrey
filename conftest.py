from typing import Optional
import pytest
from endpoints.user_request import UserRequest
from steps.user_steps import UserSteps
from data import data_test_user as test_data


@pytest.fixture()
def create_and_delete_user(): # Можно сделать такую фикстуру где и setup и teardown. Или сделать две отдельных.
    """
    Фикстура для создания пользователя перед тестом и удаления после.
    Возвращает в тест словарь с данными пользователя.
    """
    user_steps = UserSteps()
    created_user = user_steps.step_user_create_successful(**test_data.request_body_with_non_required).json()
    yield created_user
    user_steps.step_delete_user_by_id(created_user["id"])
    user_steps.step_get_user_by_id(created_user["id"], expected_status=404)


@pytest.fixture()
def delete_user():
    """
    Фикстура для удаления пользователя после теста.
    """
    user_steps = UserSteps()

    def _delete_user(user_id: int):
        """
        """
        user_steps.step_delete_user_by_id(user_id)
        user_steps.step_get_user_by_id(user_id, expected_status=404)

    return _delete_user





@pytest.fixture()
def user(request):
    user_data = request.param
    user_steps = UserSteps()
    if user_data:
        user = user_steps.step_user_create(expected_status=200, **user_data).json()
    else:
        user = user_steps.step_user_create(expected_status=200).json()

    yield user
    user_steps.step_delete_user_by_id(user.get("id"))
    user_steps.step_get_user_by_id(user.get("id"), expected_status=404)