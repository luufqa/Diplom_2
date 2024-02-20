import allure
import requests
from data.data_pages import Urls


class GetOrder:

    @allure.step('Получение списка заказов (с токеном)')
    def get_order_with_auth(self, accessToken):
        headers = {'Authorization': f'{accessToken}'}
        response = requests.get(f'{Urls.base_url}{Urls.get_order}', headers=headers)
        return response

    @allure.step('Получение списка заказов (без токена)')
    def get_order_without_auth(self):
        response = requests.get(f'{Urls.base_url}{Urls.get_order}')
        return response
