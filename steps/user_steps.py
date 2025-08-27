from checkers.user_checker import CommandChecker
from endpoints.users import UserRequest
from users import payloads


class UserSteps:
    def __init__(self):
        self.request = UserRequest()
        self.payload = payloads

    def user_create_succesfull(self, **kwargs):
        payload = self.payload.get_request_body_for_user(**kwargs)
        response = self.request.create_user_request(payload)
        CommandChecker.check_status_code(response, 200)
        CommandChecker.check_response_body(response, payload)
        return response

    def get_user_by_id(self, user_id: int, expected_status=200):
        response = self.request.get_user_request(user_id)
        CommandChecker.check_status_code(response, expected_status)
        return response

    def delete_user_by_id(self, user_id: int):
        response = self.request.delete_user_request(user_id)
        CommandChecker.check_status_code(response, 200)
        return response

