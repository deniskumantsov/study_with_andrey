import pytest
from endpoints.user_request import UserRequest
from steps.user_steps import UserSteps


@pytest.fixture()
def delete_user():

    def _delete_user(user_id):
        yield
        user_steps = UserSteps()
        user_steps.delete_user_by_id(user_id)
        user_steps.get_user_by_id(user_id, expected_status=404)




