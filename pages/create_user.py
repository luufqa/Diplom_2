import allure
import requests
import random
import string
from data.data_pages import Urls


class CreateUser:

    @allure.step('Генерация строкового значения')
    def generate_random_string(self, length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    @allure.step('Генерация данных для нового пользователя')
    def generate_user_data(self):
        email = f"{self.generate_random_string(15)}@yandex.ru"
        password = self.generate_random_string(10)
        name = self.generate_random_string(13)
        return [email, password, name]

    @allure.step('Создание пользователя. Возврат аккаунта и ответа')
    def create_user(self, account):
        payload = {
            "email": {account[0]},
            "password": {account[1]},
            "name": {account[2]}
        }
        response = requests.post(f'{Urls.base_url}{Urls.post_create_user}', data=payload)
        return account, response
