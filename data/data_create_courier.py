import pytest
from faker import Faker

fake = Faker("ru_RU")

payload_create_courier = {
    "login": f"{fake.name()}",
    "password": "1234567",
    "firstName": f"{fake.first_name()}"
}

payload_for_not_found_courier = {
    "login": f"{fake.name()}",
    "password": "1234567"
}


def data_negative_payload_for_courier():
    return [
        pytest.param({
            "password": "1234567",
            "firstName": f"{fake.first_name()}"
        }, id="payload  without login"),
        pytest.param({
            "login": f"{fake.name()}",
            "firstName": f"{fake.first_name()}"
        }, id="payload without password")

    ]


def data_delete_field():
    return [
        pytest.param("password"),
        pytest.param("login")

    ]

