import allure
from pages.create_user import CreateUser
from pages.auth_user import AuthUser


class TestAuthUser:
    @allure.title('Позитивный тест - возможно авторизовать пользователя с корректными данными')
    def test_auth_user_correct(self):
        auth_user = AuthUser()
        create_user = CreateUser()
        random_acc = create_user.generate_user_data()
        account, response = create_user.create_user(random_acc)
        result = auth_user.auth_user(account)
        # TestAuthUser.accessToken необходим для фикстуры из conftest,
        # чтобы удалить учетку после теста
        TestAuthUser.accessToken = response.json()['accessToken']
        assert result.json()['success'] == True
        assert result.status_code == 200

    @allure.title('Негативный тест - невозможно авторизовать пользователя с некорректным email')
    def test_auth_user_uncorrect_email(self):
        auth_user = AuthUser()
        create_user = CreateUser()
        random_acc = create_user.generate_user_data()
        random_acc[0] = ''
        account, response = create_user.create_user(random_acc)
        result = auth_user.auth_user(account)
        assert "email or password are incorrect" in result.json()['message']
        assert result.status_code == 401

    @allure.title('Негативный тест - невозможно авторизовать пользователя с некорректным паролем')
    def test_auth_user_uncorrect_password(self):
        auth_user = AuthUser()
        create_user = CreateUser()
        random_acc = create_user.generate_user_data()
        random_acc[1] = ''
        account, response = create_user.create_user(random_acc)
        result = auth_user.auth_user(account)
        assert "email or password are incorrect" in result.json()['message']
        assert result.status_code == 401
