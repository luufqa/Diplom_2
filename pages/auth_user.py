import allure
import requests
from data.data_pages import Urls


class AuthUser:
    @allure.step('Авторизация пользователя')
    def auth_user(self, account):
        payload = {
            "email": account[0],
            "password": account[1]
        }
        response = requests.post(f'{Urls.base_url}{Urls.post_auth_user}', data=payload)
        return response
