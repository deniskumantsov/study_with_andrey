from utils.generators import generate_valid_phone_number, generate_valid_firstname, generate_valid_lastname, \
    generate_valid_patronymic, generate_valid_birthday, generate_valid_passport_serial, generate_valid_passport_number, \
    generate_valid_password


def get_request_body_for_user(**kwargs) -> dict:
    """
    Конфигурирует тело запроса для создания пользователя.

    :return: Словарь с полями:
        - phone_number (int)
        - firstname (str)
        - lastname (str)
        - patronymic (str)
        - birthday (str)
        - passport_serial (int)
        - passport_number (int)
        - password (str)
    """
    payload = {
        "phone_number": generate_valid_phone_number(),
        "firstname": generate_valid_firstname(),
        "lastname": generate_valid_lastname(),
        "patronymic": generate_valid_patronymic(),
        "birthday": generate_valid_birthday(),
        "passport_serial": generate_valid_passport_serial(),
        "passport_number": generate_valid_passport_number(),
        "password": generate_valid_password(),
    }

    for key, value in kwargs.items():
        payload[key] = value

    return payload

# Password сейчас генерируется только потому это обязательное поле, вообще его быть не должно.
def get_request_body_for_user_update(user, **kwargs) -> dict:
    """
    Конфигурирует тело запроса для обновления пользователя.

    :return: Словарь с полями:
        - firstname (str)
        - lastname (str)
        - patronymic (str)
        - birthday (str)
        - password (str)
    """
    payload = {
        "firstname": user.get("firstname"),
        "lastname": user.get("lastname"),
        "patronymic": user.get("patronymic"),
        "birthday": user.get("birthday"),
        "password": generate_valid_password(),
    }

    for key, value in kwargs.items():
        payload[key] = value

    return payload