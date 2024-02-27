import allure
import requests
from data.data_pages import Urls


class DeleteUser:
    @allure.step('Удаление пользователя')
    def delete_user(self, accessToken):
        headers = {'Authorization': f'{accessToken}'}
        response = requests.delete(f'{Urls.base_url}{Urls.patch_edit_user}', headers=headers)
        return response
