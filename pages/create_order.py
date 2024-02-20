import allure
import requests
from data.data_pages import Urls


class CreateOrder:
    @allure.step('Создание заказа с токеном')
    def create_order_with_auth(self, ingr, access_token):
        headers = {'Authorization': f'{access_token}'}
        payload = {
            "ingredients": ingr
        }
        response = requests.post(f'{Urls.base_url}{Urls.post_create_order}', headers=headers, data=payload)
        return response

    @allure.step('Создание заказа без токена')
    def create_order_without_auth(self, ingr):
        payload = {
            "ingredients": ingr
        }
        response = requests.post(f'{Urls.base_url}{Urls.post_create_order}', data=payload)
        return response
