import allure
from pages.create_user import CreateUser
from pages.auth_user import AuthUser
from pages.create_order import CreateOrder
from pages.get_ingredients import GetIngredients


class TestCreateOrderWithAuth:
    @allure.title('Позитивный тест - возможно создать заказ (с токеном)')
    def test_create_order_with_auth_correct(self):
        create_order = CreateOrder()
        create_user = CreateUser()
        auth_user = AuthUser()
        get_ingredients = GetIngredients()
        ingrs = get_ingredients.get_ingredients()
        random_acc = create_user.generate_user_data()
        account, response = create_user.create_user(random_acc)
        result = auth_user.auth_user(account)
        TestCreateOrderWithAuth.accessToken = result.json()['accessToken']
        res_create = create_order.create_order_with_auth(ingrs, TestCreateOrderWithAuth.accessToken)
        assert res_create.json()['success'] == True
        assert res_create.status_code == 200

    @allure.title('Негативный тест - невозможно создать заказ без ингредиентов (с токеном)')
    def test_create_order_with_auth_empty(self):
        create_order = CreateOrder()
        create_user = CreateUser()
        auth_user = AuthUser()
        ingrs = []
        random_acc = create_user.generate_user_data()
        account, response = create_user.create_user(random_acc)
        result = auth_user.auth_user(account)
        TestCreateOrderWithAuth.accessToken = result.json()['accessToken']
        res_create = create_order.create_order_with_auth(ingrs, TestCreateOrderWithAuth.accessToken)
        assert res_create.json()['message'] == "Ingredient ids must be provided"
        assert res_create.status_code == 400

    @allure.title('Негативный тест - невозможно создать заказ с неверным хешем ингредиентов (с токеном)')
    def test_create_order_with_auth_uncorrect(self):
        create_order = CreateOrder()
        create_user = CreateUser()
        auth_user = AuthUser()
        ingrs = ['s1394840s']
        random_acc = create_user.generate_user_data()
        account, response = create_user.create_user(random_acc)
        result = auth_user.auth_user(account)
        TestCreateOrderWithAuth.accessToken = result.json()['accessToken']
        res_create = create_order.create_order_with_auth(ingrs, TestCreateOrderWithAuth.accessToken)
        assert "<!DOCTYPE html>" in res_create.text
        assert res_create.status_code == 500


class TestCreateOrderWithoutAuth:
    @allure.title('Позитивный тест - возможно создать заказ (без токена)')
    def test_create_order_without_auth_correct(self):
        create_order = CreateOrder()
        get_ingredients = GetIngredients()
        ingrs = get_ingredients.get_ingredients()
        res_create = create_order.create_order_without_auth(ingrs)
        assert res_create.json()['success'] == True
        assert res_create.status_code == 200

    @allure.title('Негативный тест - невозможно создать заказ без ингредиентов (без токена)')
    def test_create_order_without_auth_empty(self):
        create_order = CreateOrder()
        ingrs = []
        res_create = create_order.create_order_without_auth(ingrs)
        assert res_create.json()['message'] == "Ingredient ids must be provided"
        assert res_create.status_code == 400

    @allure.title('Негативный тест - невозможно создать заказ с неверным хешем ингредиентов (без токена)')
    def test_create_order_without_auth_uncorrect(self):
        create_order = CreateOrder()
        ingrs = ['s1394840s']
        res_create = create_order.create_order_without_auth(ingrs)
        assert "<!DOCTYPE html>" in res_create.text
        assert res_create.status_code == 500
