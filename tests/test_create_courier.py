import allure
import pytest

from endpoint.couriers.create_courier import CreateCourier
from endpoint.couriers.delete_courier import DeleteCourier
from endpoint.couriers.get_courier_id import GetCourierId
from data.data_create_courier import data_negative_payload_for_courier, payload_create_courier


class TestCreateCourier:
    @allure.feature('Создание курьера')
    @allure.story('Создание курьера')
    @allure.suite('Создание курьера')
    @allure.sub_suite('Позитивные данные')
    @allure.title('Создание курьера')
    @allure.description('курьера можно создать')
    def test_create_courier(self):
        create = CreateCourier()
        create.create_courier(payload_create_courier)
        create.response_is(201)
        create.response_json_is({'ok': True})

        get = GetCourierId()
        get.get_id(payload_create_courier)
        delete = DeleteCourier()
        delete.delete_courier(get.id)
        delete.response_is(200)

    @allure.feature('Создание курьера')
    @allure.story('Позитивные данные')
    @allure.suite('Создание курьера')
    @allure.sub_suite('Позитивные данные')
    @allure.title('Проверка, что курьер создан')
    @allure.description('Проверка создания курьера')
    def test_check_new_courier(self, prepare_courier):
        get = GetCourierId()
        get.get_id(prepare_courier[1])
        with allure.step('id созданного и id полученное из базы по данным совпадают '):
            assert prepare_courier[0] == get.id

    @allure.feature('Создание курьера')
    @allure.story('Негативные данные')
    @allure.suite('Создание курьера')
    @allure.sub_suite('Негативные данные')
    @allure.title('Дублирование регистрации')
    @allure.description('Нельзя создать двух одинаковых курьеров')
    def test_create_double_courier(self, prepare_courier):
        create = CreateCourier()
        create.create_courier(prepare_courier[1])
        create.response_is(409)
        create.response_json_is({'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'})

    @allure.feature('Создание курьера')
    @allure.story('Негативные данные')
    @allure.suite('Создание курьера')
    @allure.sub_suite('Негативные данные')
    @allure.description('чтобы создать курьера, нужно передать в ручку все обязательные поля')
    @allure.title('Отсутствие обязательных полей')
    @pytest.mark.parametrize('test_payload', data_negative_payload_for_courier())
    def test_create_courier_bad_payload(self, test_payload):
        create = CreateCourier()
        create.create_courier(test_payload)
        create.response_is(400)
        create.response_json_is({'code': 400, 'message': 'Недостаточно данных для создания учетной записи'})
