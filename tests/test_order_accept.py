import allure

from endpoint.orders.accept_order import AcceptOrder


class TestOrderAccept:
    @allure.feature('Заказы')
    @allure.story('Прием заказа')
    @allure.suite('Прием заказа')
    @allure.sub_suite('Позитивные данные')
    @allure.title('Прием заказа с верными данными')
    @allure.description('Прием заказа с верными данными. Тест иногда падает, потому что Api возвращает, что нет '
                        'такого заказа, хотя при проверке через получение заказа -заказ есть')
    def test_accept_order(self, prepare_courier, prepare_order):
        accept_order = AcceptOrder()
        accept_order.accept_order(prepare_order,  prepare_courier[0])
        accept_order.response_is(200)
        accept_order.response_json_is({"ok": True})

    @allure.feature('Заказы')
    @allure.story('Прием заказа')
    @allure.suite('Прием заказа')
    @allure.sub_suite('Негативные данные')
    @allure.title('Id курьера неверный')
    @allure.description('Прием заказа с неверным ID курьера')
    def test_accept_order_bad_id_courier(self, prepare_courier, prepare_order):
        accept_order = AcceptOrder()
        accept_order.accept_order(prepare_order,  prepare_courier[0] + 100000)
        accept_order.response_is(404)
        accept_order.response_json_is({'code': 404, 'message': 'Курьера с таким id не существует'})

    @allure.feature('Заказы')
    @allure.story('Прием заказа')
    @allure.suite('Прием заказа')
    @allure.sub_suite('Негативные данные')
    @allure.title('Id заказа неверный')
    @allure.description('Прием заказа с неверным ID заказа')
    def test_accept_order_bad_id_order(self, prepare_courier, prepare_order):
        accept_order = AcceptOrder()
        accept_order.accept_order(prepare_order + 1000000,  prepare_courier[0])
        accept_order.response_is(404)
        accept_order.response_json_is({'code': 404, 'message': 'Заказа с таким id не существует'})

    @allure.feature('Заказы')
    @allure.story('Прием заказа')
    @allure.suite('Прием заказа')
    @allure.sub_suite('Негативные данные')
    @allure.title('Id заказа не задан')
    @allure.description('Прием заказа без ID заказа. В описании ошибка должна быть 400 Недостаточно данных для '
                        'поиска, на самом деле возвращает 404 Not Found, но в задании проверить, что вернет ошибку')
    def test_accept_order_without_id_order(self, prepare_courier, prepare_order):
        accept_order = AcceptOrder()
        accept_order.accept_order(courier_id= prepare_courier[0])
        accept_order.response_is(404)
        accept_order.response_json_is({'code': 404, 'message': 'Not Found.'})

    @allure.feature('Заказы')
    @allure.story('Прием заказа')
    @allure.suite('Прием заказа')
    @allure.sub_suite('Негативные данные')
    @allure.title('Id курьера не задан')
    @allure.description('Прием заказа без ID курьера')
    def test_accept_order_without_id_courier(self, prepare_courier, prepare_order):
        accept_order = AcceptOrder()
        accept_order.accept_order(track_id=prepare_courier)
        accept_order.response_is(400)
        accept_order.response_json_is({'code': 400, 'message': 'Недостаточно данных для поиска'})
