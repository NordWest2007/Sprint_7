import pytest
from faker import Faker

fake = Faker("ru_RU")


def data_for_orders():
    return [
        pytest.param({
            "firstName": fake.first_name(),
            "lastName": fake.last_name(),
            "address": fake.address(),
            "metroStation": 5,
            "phone": fake.phone_number(),
            "rentTime": 5,
            "deliveryDate": fake.date(),
            "comment": "комментарий",
            "color": [
                "BLACK"
            ]
        }, id="color BLACK"),
        pytest.param({
            "firstName": fake.first_name(),
            "lastName": fake.last_name(),
            "address": fake.address(),
            "metroStation": 5,
            "phone": fake.phone_number(),
            "rentTime": 5,
            "deliveryDate": fake.date(),
            "comment": "комментарий",
            "color": [
                "GREY"
            ]
        }, id="color GREY"),
        pytest.param({
            "firstName": fake.first_name(),
            "lastName": fake.last_name(),
            "address": fake.address(),
            "metroStation": 5,
            "phone": fake.phone_number(),
            "rentTime": 5,
            "deliveryDate": fake.date(),
            "comment": "комментарий",
            "color": [
                "GREY",
                "BLACK"
            ]
        }, id="color GREY,BLACK"),
        pytest.param({
            "firstName": fake.first_name(),
            "lastName": fake.last_name(),
            "address": fake.address(),
            "metroStation": 5,
            "phone": fake.phone_number(),
            "rentTime": 5,
            "deliveryDate": fake.date(),
            "comment": "комментарий"
        }, id="without color")

    ]


payload_order = {
    "firstName": fake.first_name(),
    "lastName": fake.last_name(),
    "address": fake.address(),
    "metroStation": 5,
    "phone": fake.phone_number(),
    "rentTime": 5,
    "deliveryDate": fake.date(),
    "comment": "комментарий",
    "color": [
        "BLACK"
    ]
}
