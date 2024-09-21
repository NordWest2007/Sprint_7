import allure

from endpoint.orders.get_order import GetOrder


class TestOrderGet:

    @allure.feature('Заказы')
    @allure.story('Получение заказа')
    @allure.suite('Получение заказа')
    @allure.sub_suite('Позитивные данные')
    @allure.title('Получение заказа')
    @allure.description('Получение заказа по его номеру')
    def test_get_order(self,prepare_order):
        order = GetOrder()
        order.get_order_by_id(prepare_order)
        order.response_is(200)
        with allure.step('Информация о заказе есть в ответе'):
            assert 'order' in order.response.json()

    @allure.feature('Заказы')
    @allure.story('Получение заказа')
    @allure.suite('Получение заказа')
    @allure.sub_suite('Негативные данные')
    @allure.title('Несуществующий номер')
    @allure.description('С неверным номером заказа')
    def test_get_order_bad_id_order(self,prepare_order):
        order = GetOrder()
        order.get_order_by_id(prepare_order + 100000)
        order.response_is(404)
        order.response_json_is({'code': 404, 'message': 'Заказ не найден'})

    @allure.feature('Заказы')
    @allure.story('Получение заказа')
    @allure.suite('Получение заказа')
    @allure.sub_suite('Негативные данные')
    @allure.title('Без номера заказа')
    @allure.description('Не задан номер заказа')
    def test_get_order_without_id_order(self,prepare_order):
        order = GetOrder()
        order.get_order_by_id()
        order.response_is(400)
        order.response_json_is({'code': 400, 'message': 'Недостаточно данных для поиска'})
