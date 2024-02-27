import allure
import requests
from data.data_pages import Urls


class GetIngredients:

    @allure.step('Получение списка ингредиентов')
    def get_ingredients(self):
        ingr = []
        response = requests.get(f'{Urls.base_url}{Urls.get_ingredients}')
        for ids in response.json()['data']:
            ingr.append(ids['_id'])
        return ingr
