import allure
import pytest
from pages.create_user import CreateUser
from data.data_pages import Fields


class TestCreateUser:
    @allure.title('Позитивный тест - возможно создать уникального пользователя')
    def test_create_user_correct(self):
        create_user = CreateUser()
        random_acc = create_user.generate_user_data()
        account, response = create_user.create_user(random_acc)
        # TestCreateUser.accessToken необходим для фикстуры из conftest,
        # чтобы удалить учетку после теста
        TestCreateUser.accessToken = response.json()['accessToken']
        assert response.json()['success'] == True
        assert response.status_code == 200

    @allure.title('Негативный тест - невозможно создать пользователя, который уже зарегистрирован')
    def test_create_user_identic(self):
        create_user = CreateUser()
        random_acc = create_user.generate_user_data()
        account, response = create_user.create_user(random_acc)
        identic_register, response = create_user.create_user(account)
        assert response.json()['message'] == 'User already exists'
        assert response.status_code == 403

    @allure.title('Негативный тест - невозможно создать пользователя и не заполнить одно из обязательных полей')
    @pytest.mark.parametrize("account_data, expected",
                             [(Fields.empty_email, Fields.error_data),
                              (Fields.empty_password, Fields.error_data),
                              (Fields.empty_name, Fields.error_data)])
    def test_create_courier_uncorrect(self, account_data, expected):
        create_user = CreateUser()
        account, response = create_user.create_user(account_data)
        assert response.json()['message'] == expected
        assert response.status_code == 403
