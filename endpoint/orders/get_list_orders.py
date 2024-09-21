import allure
import requests

from endpoint.base_endpoint import BaseEndpoint
from data.costants import Constants


class GetListOrders(BaseEndpoint):
    response = None
    status = None
    response_json = None

    def get_orders(self):
        with allure.step('Получение  списка всех заказов'):
            self.response = requests.get(f"{Constants.BASE_URL}{Constants.CREATE_ORDER_URL}")
            self.status = self.response.status_code
            self.response_json = self.response.json()