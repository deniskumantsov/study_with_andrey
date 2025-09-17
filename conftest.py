from typing import Optional
import pytest
from endpoints.user_request import UserRequest
from steps.user_steps import UserSteps
from data import data_test_user as test_data


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
def user(request):
    """

    :param request:
    :return:
    """
    user_data = request.param
    user_steps = UserSteps()
    if user_data == "random":
        user = user_steps.step_valid_user_create().json()
    else:
        user = user_steps.step_valid_user_create(**user_data).json()

    yield user
    user_steps.step_delete_user_by_id(user.get("id"))
    # user_steps.step_get_user_by_id(user.get("id"), expected_status=404) # Можно вообще отказаться здесь от гета, т.к это проверится в тестах и делит заведомо исправен.
    # в гете оставить лучше expected статус оставить чтобы не горадить с ним потом.