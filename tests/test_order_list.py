import allure

from endpoint.orders.get_list_orders import GetListOrders


class TestOrderList:

    @allure.feature('Заказы')
    @allure.story('Получение списка заказов')
    @allure.suite('Заказы')
    @allure.sub_suite('Позитивные данные')
    @allure.title('Список содержит заказы')
    @allure.description('Получение списка заказов. Проверка, что ответ содержит заказы')
    def test_list_orders(self):
        list_order = GetListOrders()
        list_order.get_orders()
        list_order.response_is(200)
        with allure.step('Список содержит заказы'):
            assert 'orders' in list_order.response.json()
