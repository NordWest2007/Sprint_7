import allure
import pytest

from endpoint.couriers.get_courier_id import GetCourierId
from data.data_create_courier import payload_for_not_found_courier, data_delete_field


class TestLoginCourier:

    @allure.feature('Авторизация курьера')
    @allure.story(' данные')
    @allure.suite('Авторизация курьера')
    @allure.sub_suite('Позитивные данные')
    @allure.title('Авторизация курьера')
    @allure.description('Курьер, имеющий регистрацию может авторизоваться')
    def test_authorization_courier(self, prepare_courier):
        get = GetCourierId()
        get.get_id(prepare_courier[1])
        get.response_is(200)
        with allure.step('Зарегистрированный курьер авторизован'):
            assert get.response_json['id'] == prepare_courier[0]

    @allure.feature('Авторизация курьера')
    @allure.story('Негативные данные')
    @allure.suite('Авторизация курьера')
    @allure.sub_suite('Негативные данные')
    @allure.title('Несуществующий курьер')
    @allure.description('Авторизация несуществующего курьера')
    def test_authorization_bad_courier(self):
        get = GetCourierId()
        get.get_id(payload_for_not_found_courier)
        get.response_is(404)
        get.response_json_is({'code': 404, 'message': 'Учетная запись не найдена'})

    @allure.feature('Авторизация курьера')
    @allure.story('Негативные данные')
    @allure.suite('Авторизация курьера')
    @allure.sub_suite('Негативные данные')
    @allure.description('система вернёт ошибку, если неправильно указать логин или пароль;')
    @allure.title('Ошибки в данным')
    @pytest.mark.parametrize('test_payload', data_delete_field())
    def test_authorization_bad_courier(self, prepare_courier, test_payload):
        get = GetCourierId()
        bad_payload = prepare_courier[1].copy()
        bad_payload[test_payload] = bad_payload[test_payload] + '-не существует'
        get.get_id(bad_payload)
        get.response_is(404)
        get.response_json_is({'code': 404, 'message': 'Учетная запись не найдена'})

    @allure.feature('Авторизация курьера')
    @allure.story('Негативные данные')
    @allure.suite('Авторизация курьера')
    @allure.sub_suite('Негативные данные')
    @allure.title('Отсутствие обязательных полей')
    @allure.description(
        'Параметризованный тест, что для авторизации нужно передать все обязательные поля. Если не задать '
        'пароль, то запрос падает в 504 ошибку, вместо обработки и ответа 400. ')
    @pytest.mark.parametrize('test_payload', data_delete_field())
    def test_authorization_courier_without_requirement_field(self, prepare_courier, test_payload):
        get = GetCourierId()
        bad_payload = prepare_courier[1].copy()
        del bad_payload[test_payload]
        get.get_id(bad_payload)
        get.response_is(400)
        get.response_json_is({'code': 400, 'message': 'Недостаточно данных для входа'})
