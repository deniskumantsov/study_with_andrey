from utils.generators import generate_valid_phone_number


request_body = {
        "phone_number": generate_valid_phone_number(),
        "firstname": "Денис",
        "lastname": "Куманцов",
        "patronymic": "Игоревич",
        "birthday": "1999-09-03",
        "passport_serial": 1234,
        "passport_number": 567890,
        "password": "Qwerty!123"
}