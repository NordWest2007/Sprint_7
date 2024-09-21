import allure

from endpoint.couriers.delete_courier import DeleteCourier


class TestDeleteCourier:
    @allure.feature('Удаление курьера')
    @allure.story('Удаление курьера')
    @allure.suite('Удаление курьера')
    @allure.sub_suite('Позитивные данные')
    @allure.title('Удаление курьера')
    @allure.description('курьера можно удалить')
    def test_delete_courier(self, create_courier_for_test_delete):
        delete = DeleteCourier()
        delete.delete_courier(create_courier_for_test_delete)
        delete.response_is(200)
        delete.response_json_is({"ok": True})

    @allure.feature('Удаление курьера')
    @allure.story('Удаление курьера')
    @allure.suite('Удаление курьера')
    @allure.sub_suite('Негативные данные')
    @allure.title('Неверный Id')
    @allure.description('Удаление курьера с неверным id')
    def test_delete_without_id(self, prepare_courier):
        delete = DeleteCourier()
        delete.delete_courier(prepare_courier[0] + 100000)
        delete.response_is(404)
        delete.response_json_is({'code': 404, 'message': 'Курьера с таким id нет.'})

    @allure.feature('Удаление курьера')
    @allure.story('Удаление курьера')
    @allure.suite('Удаление курьера')
    @allure.sub_suite('Негативные данные')
    @allure.title('Id не указан')
    @allure.description('Удаление без указания id возвращает ошибку')
    def test_delete_without_id(self, prepare_courier):
        delete = DeleteCourier()
        delete.delete_courier()
        delete.response_is(404)
        delete.response_json_is({'code': 404, 'message': 'Not Found.'})
