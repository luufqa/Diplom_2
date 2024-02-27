import allure
import requests
from data.data_pages import Urls


class EditUser:
    @allure.step('Частичное изменение данных пользователя (с токеном)')
    def patch_edit_user_with_auth(self, accessToken, user_key, expected):
        headers = {'Authorization': f'{accessToken}'}
        payload = {
            f'{user_key}': f'{expected}'
        }
        response = requests.patch(f'{Urls.base_url}{Urls.patch_edit_user}', headers=headers, data=payload)
        return response

    @allure.step('Частичное изменение данных пользователя (без токена)')
    def patch_edit_user_without_auth(self, user_key, expected):
        payload = {
            f'{user_key}': f'{expected}'
        }
        response = requests.patch(f'{Urls.base_url}{Urls.patch_edit_user}', data=payload)
        return response
