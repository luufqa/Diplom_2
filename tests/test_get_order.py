import allure
from pages.create_user import CreateUser
from pages.auth_user import AuthUser
from pages.get_order import GetOrder


class TestGetOrder:

    @allure.title('Позитивный тест - возможно получить список заказов (с токеном)')
    def test_get_order_with_auth(self):
        create_user = CreateUser()
        auth_user = AuthUser()
        get_order = GetOrder()
        random_acc = create_user.generate_user_data()
        account, response = create_user.create_user(random_acc)
        result = auth_user.auth_user(account)
        TestGetOrder.accessToken = result.json()['accessToken']
        res_get = get_order.get_order_with_auth(TestGetOrder.accessToken)
        assert res_get.json()['success'] == True
        assert res_get.status_code == 200

    @allure.title('Негативный тест - невозможно получить список заказов (без токена)')
    def test_get_order_without_auth(self):
        get_order = GetOrder()
        res_get = get_order.get_order_without_auth()
        assert res_get.json()['message'] == 'You should be authorised'
        assert res_get.status_code == 401
