import allure
import requests

from endpoint.base_endpoint import BaseEndpoint
from data.costants import Constants


class GetOrderTrack(BaseEndpoint):
    response = None
    status = None
    response_json = None

    def get_track(self, payload):
        with allure.step('Получение  номера заказа'):
            self.response = requests.post(f"{Constants.BASE_URL}{Constants.GET_ORDER_TRACK_URL}", data=payload)
            self.status = self.response.status_code
            self.response_json = self.response.json()
