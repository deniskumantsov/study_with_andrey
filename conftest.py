from typing import Optional

import pytest
from endpoints.user_request import UserRequest
from steps.user_steps import UserSteps


@pytest.fixture()
def delete_user():
    """

    """
    def _delete_user(user_id):
        yield
        user_steps = UserSteps()
        user_steps.delete_user_by_id(user_id)
        user_steps.get_user_by_id(user_id, expected_status=404)
    return _delete_user


@pytest.fixture()
def entity_collector():
    """

    """
    created_users = []

    def delete_track_user(user_data_response):
        if user_data_response.status_code == 200:
            created_users.append(user_data_response.json()["id"])

    yield delete_track_user

    steps = UserSteps()
    for user_id in created_users:
        steps.delete_user_by_id(user_id)
        steps.get_user_by_id(user_id, expected_status=404)


@pytest.fixture()
def user(request):
    user_data = request.param
    user_steps = UserSteps()
    if user_data:
        user = user_steps.user_create(expected_status=200, **user_data).json()
    else:
        user = user_steps.user_create(expected_status=200).json()

    yield user
    user_steps.delete_user_by_id(user.get("id"))
    user_steps.get_user_by_id(user.get("id"), expected_status=404)