import allure
import pytest

from endpoint.orders.create_order import CreateOrder
from endpoint.orders.delete_order import DeleteOrder
from data.data_orders import data_for_orders


class TestOrderCreate:
    @allure.feature('Заказы')
    @allure.story('Создание заказа')
    @allure.suite('Заказы')
    @allure.sub_suite('Позитивные данные')
    @allure.title('Проверка поля color')
    @allure.description(
        'Параметризованный тест, при создании заказа можно не указывать цвет, указать один или несколько '
        'цветов')
    @pytest.mark.parametrize('test_payload', data_for_orders())
    def test_create_order(self, test_payload):
        create = CreateOrder()
        create.create_order(test_payload)
        create.response_is(201)
        with allure.step('Тело ответа содержит track'):
            assert 'track' in create.response_json

        delete = DeleteOrder()
        delete.cancel_order(create.response_json)
        delete.response_is(200)
