import allure
from checkers.common_checkers import CommonChecker
from endpoints.user_request import UserRequest
from users import user_payload
from collections import defaultdict, namedtuple
# defaultdict — это словарь, который автоматически создает значение по умолчанию для нового ключа. Здесь будет
# использоваться для хранения пользователей.
# namedtuple — это «именованный кортеж», который ведет себя как обычный кортеж, но позволяет обращаться к полям по имени
# (id, name, notes) вместо индекса.


UserShortInfo = namedtuple("UserShortInfo", ["id", "name", "notes"])
# ["id", "name", "notes"] поля объекта
# id  уникальный ид пользователя.
# name имя пользователя (в примере берётся firstname).
# notes поле для дополнительных пометок, например "deleted", чтобы помечать пользователей, которых нужно удалить.
class DataCollector:
    _data_dict = defaultdict(list)  # глобальное хранилище для всех экземпляров

    def __init__(self):
        self.__dict__ = self._data_dict

    def collect(self, entity: dict):
        """

        :param entity:
        """
        user_info = UserShortInfo(id=entity["id"], name=entity["firstname"], notes=None)
        self._data_dict["users"].append(user_info)
        # Метод возьмёт из словаря(из созданного юзера грубо говоря) только поля id и firstname для name,
        # Создаст объект UserShortInfo(id=..., name=..., notes=None),
        # И добавит его в список _data_dict["users"].

    def update(self, entity_id: int, info: str = "deleted"):
        """

        :param entity_id:
        :param info:
        :return:
        """
        updated_list = []
        for entity in self._data_dict["users"]:
            if entity.id == entity_id:
                updated_list.append(entity._replace(notes=info))
            else:
                updated_list.append(entity)
        self._data_dict["users"] = updated_list



class UserSteps:
    """
    Класс-обертка над UserRequest.
    Содержит бизнес шаги.
    """
    def __init__(self):
        self.request = UserRequest()
        self.payload = user_payload

    @allure.step("Получить список всех пользователей.")
    def step_get_users(self):
        """
        Получить список всех пользователей.

        :return: Объект Response.
        """
        response = self.request.get_users_request()
        CommonChecker.check_status_code_ok(response)
        return response


    @allure.step("Создать валидного пользователя.")
    def step_valid_user_create(self, **kwargs):
        """
        Создать валидного пользователя.

        :param kwargs: Параметры для конфигурации тела запроса.
        :return: Объект Response.
        """
        payload = self.payload.get_request_body_for_user(**kwargs)
        response = self.request.create_user_request(payload)
        # здесь будет коллектор
        CommonChecker.check_status_code_ok(response)
        return response


    @allure.step("Создать невалидного пользователя.")
    def step_invalid_user_create(self, **kwargs):
        """
        Создать невалидного пользователя.

        :param kwargs: Параметры для конфигурации тела запроса.
        :return: Объект Response.
        """
        payload = self.payload.get_request_body_for_user(**kwargs)
        response = self.request.create_user_request(payload)

        if response.status_code == 200:
            user_id = response.json().get("id")
            Collector.add(user_id)

        CommonChecker.check_status_code_422(response) # В теории можно вообще здесь не чекать статус код
        return response


    @allure.step("Получить пользователя по ID.")
    def step_get_user_by_id(self, user_id: int, expected_status: int = 200):
        """
        Получить пользователя по ID.

        :param user_id: ID пользователя.
        :return: Объект Response.
        """
        response = self.request.get_user_request(user_id)
        # здесь будет коллектор
        if expected_status == 200:
            CommonChecker.check_status_code_ok(response)
        elif expected_status == 422:
            CommonChecker.check_status_code_422(response)
        elif expected_status == 404:
            CommonChecker.check_status_code_404(response)
        return response


    @allure.step("Обновить данные пользователя по ID валидными данными.")
    def step_update_user_by_id_with_valid_fields(self, user: dict, **kwargs):
        """
        Обновить данные пользователя по ID валидными данными.
        :param user: Словарь с данными пользователя.
        :param kwargs: Параметры для конфигурации тела запроса.
        :return: Объект Response.
        """
        payload = self.payload.get_request_body_for_user_update(user, **kwargs)
        response = self.request.update_user_request(user.get("id"), payload)
        # здесь будет коллектор
        CommonChecker.check_status_code_ok(response)
        return response


    @allure.step("Обновить данные пользователя по ID невалидными данными.")
    def step_update_user_by_id_with_invalid_fields(self, user: dict, **kwargs):
        """
        Обновить данные пользователя по ID невалидными данными.
        :param user: Словарь с данными пользователя.
        :param kwargs: Параметры для конфигурации тела запроса.
        :return: Объект Response.
        """
        payload = self.payload.get_request_body_for_user_update(user, **kwargs)
        response = self.request.update_user_request(user.get("id"), payload)
        # здесь будет коллектор
        CommonChecker.check_status_code_422(response)
        return response


    @allure.step("Удалить пользователя по ID.")
    def step_delete_user_by_id(self, user_id: int):
        """
        Удалить пользователя по ID.

        :param user_id: ID пользователя.
        :return: Объект Response.
        """
        response = self.request.delete_user_request(user_id)
        CommonChecker.check_status_code_ok(response)
        return response