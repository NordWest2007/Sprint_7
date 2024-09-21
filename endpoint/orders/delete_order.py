import allure
import requests

from endpoint.base_endpoint import BaseEndpoint
from data.costants import Constants


class DeleteOrder(BaseEndpoint):
    status = None
    response_json = None
    response = None

    def cancel_order(self, track_id):
        with allure.step('Удаление заказа по track'):
            self.response = requests.put(f"{Constants.BASE_URL}{Constants.DELETE_ORDER_URL}",params=track_id)
            self.status = self.response.status_code
            self.response_json = self.response.json()
