import allure
import requests

from endpoint.base_endpoint import BaseEndpoint
from data.costants import Constants


class CreateCourier(BaseEndpoint):
    status = None
    response_json = None


    def create_courier(self, payload) -> None:
        with allure.step('Создание курьера. Отправка запроса'):
            self.response = requests.post(f'{Constants.BASE_URL}{Constants.CREATE_COURIER_URL}', data=payload)
            self.status = self.response.status_code
            self.response_json = self.response.json()

