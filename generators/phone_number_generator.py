import time


def generate_valid_phone_number():
    timestamp = int(time.time() * 1000)
    phone_number = str(timestamp)[-10:]
    return int(phone_number)
print(generate_valid_phone_number())


def generate_invalid_phone_number_nine():
    timestamp = int(time.time() * 1000)
    phone_number = str(timestamp)[-9:]
    return int(phone_number)
print(generate_invalid_phone_number_nine())


def generate_invalid_phone_number_eleven():
    timestamp = int(time.time() * 1000)
    phone_number = str(timestamp)[-11:]
    return int(phone_number)
print(generate_invalid_phone_number_eleven())


def generate_invalid_phone_number_str():
    timestamp = int(time.time() * 1000)
    phone_number = str(timestamp)[-11:]
    return f'+7{int(phone_number)}'
print(generate_invalid_phone_number_str())


def generate_invalid_phone_number_none():
    return None

