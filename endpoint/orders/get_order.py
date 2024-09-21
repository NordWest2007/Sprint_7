import allure
import requests

from endpoint.base_endpoint import BaseEndpoint
from data.costants import Constants


class GetOrder(BaseEndpoint):
    response = None
    status = None
    response_json = None

    def get_order_by_id(self, id_order=None):
        with allure.step('Получение  заказа по id'):
            self.response = requests.get(f"{Constants.BASE_URL}{Constants.GET_ORDER_BY_ID}", params={"t": id_order})
            self.status = self.response.status_code
            self.response_json = self.response.json()
