import allure
import requests

from endpoint.base_endpoint import BaseEndpoint
from data.costants import Constants


class DeleteCourier(BaseEndpoint):
    status = None
    response_json = None
    response = None

    def delete_courier(self, id_courier=''):
        with allure.step('Удаление курьера по id'):
            self.response = requests.delete(f"{Constants.BASE_URL}{Constants.DELETE_COURIER_URL}/{id_courier}")
            self.status = self.response.status_code
            self.response_json = self.response.json()
