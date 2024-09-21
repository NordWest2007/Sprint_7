import allure
import requests

from endpoint.base_endpoint import BaseEndpoint
from data.costants import Constants


class AcceptOrder(BaseEndpoint):
    status = None
    response_json = None
    response = None

    def accept_order(self, track_id='',courier_id=''):
        with allure.step('принятие заказа '):
            self.response = requests.put(f"{Constants.BASE_URL}{Constants.ACCEPT_ORDER_URL}{track_id}",params={"courierId":courier_id})
            self.status = self.response.status_code
            self.response_json = self.response.json()
