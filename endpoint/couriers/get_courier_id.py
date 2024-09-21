import allure
import requests

from endpoint.base_endpoint import BaseEndpoint
from data.costants import Constants


class GetCourierId(BaseEndpoint):
    response = None
    status = None
    id = None
    response_json = None

    def get_id(self, payload):
        with allure.step('Получение  id курьера'):
            self.response = requests.post(f"{Constants.BASE_URL}{Constants.GET_COURIER_ID_URL}", data=payload)
            self.status = self.response.status_code
            if self.status == 200:
                self.id = self.response.json()['id']
            if self.status == 504:
                self.response_json = ''
            else:
                self.response_json = self.response.json()
