import allure
import pytest
from pages.create_user import CreateUser
from pages.auth_user import AuthUser
from pages.edit_user import EditUser


class TestEditUserWithAuth():

    @pytest.mark.parametrize("user_key, expected",
                             [('email', CreateUser().generate_user_data()[0]),
                              ('name', CreateUser().generate_user_data()[2])])
    @allure.title('Позитивный тест - возможно изменить данные пользователя (с токеном)')
    def test_edit_user_with_auth(self, user_key, expected):
        create_user = CreateUser()
        auth_user = AuthUser()
        edit_user = EditUser()
        random_acc = create_user.generate_user_data()
        account, response = create_user.create_user(random_acc)
        result = auth_user.auth_user(account)
        # TestEditUserWithAuth.accessToken необходим для фикстуры из conftest,
        # чтобы удалить учетку после теста
        TestEditUserWithAuth.accessToken = result.json()['accessToken']
        res_patch = edit_user.patch_edit_user_with_auth(TestEditUserWithAuth.accessToken, user_key, expected)
        assert res_patch.json()['user'][user_key] == expected
        assert res_patch.status_code == 200


class TestEditUserWithoutAuth:
    @pytest.mark.parametrize("user_key, expected",
                             [('email', CreateUser().generate_user_data()[0]),
                              ('name', CreateUser().generate_user_data()[2])])
    @allure.title('Негативный тест - невозможно изменить данные пользователя (без токена)')
    def test_edit_user_without_auth(self, user_key, expected):
        create_user = CreateUser()
        edit_user = EditUser()
        random_acc = create_user.generate_user_data()
        account, response = create_user.create_user(random_acc)
        # TestEditUserWithoutAuth.accessToken необходим для фикстуры из conftest,
        # чтобы удалить учетку после теста
        TestEditUserWithoutAuth.accessToken = response.json()['accessToken']
        res_patch = edit_user.patch_edit_user_without_auth(user_key, expected)
        assert res_patch.json()['message'] == "You should be authorised"
        assert res_patch.status_code == 401
