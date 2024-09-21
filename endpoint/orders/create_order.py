import allure
import requests

from endpoint.base_endpoint import BaseEndpoint
from data.costants import Constants


class CreateOrder(BaseEndpoint):
    status = None
    response_json = None
    track= None

    def create_order(self, payload) -> None:
        with allure.step('Создание заказа. Отправка запроса'):
            self.response = requests.post(f"{Constants.BASE_URL}{Constants.CREATE_ORDER_URL}", json=payload)
            self.status = self.response.status_code
            self.response_json = self.response.json()
            if self.status == 201:
                self.track = self.response_json['track']
