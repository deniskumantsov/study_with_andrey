from checkers.common_checkers import CommonChecker
from checkers.user_checkers import UserChecker
from endpoints.user_request import UserRequest
from users import user_payload


class UserSteps:
    """

    """
    def __init__(self):
        self.request = UserRequest()
        self.payload = user_payload

    def user_create_successful(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        payload = self.payload.get_request_body_for_user(**kwargs)
        response = self.request.create_user_request(payload)
        CommonChecker.check_status_code(response, 200)
        UserChecker.check_response_body(response, payload)
        return response


    def get_user_by_id(self, user_id: int, expected_status=200):
        """

        :param user_id:
        :param expected_status:
        :return:
        """
        response = self.request.get_user_request(user_id)
        CommonChecker.check_status_code(response, expected_status)
        return response


    def delete_user_by_id(self, user_id: int):
        """

        :param user_id:
        :return:
        """
        response = self.request.delete_user_request(user_id)
        CommonChecker.check_status_code(response, 200)
        return response

