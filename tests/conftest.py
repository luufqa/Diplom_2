import pytest
from pages.delete_user import DeleteUser
@pytest.fixture(autouse=True)
def fixture(request):
    yield
    if request.node.name in ["test_auth_user_correct", "test_create_user_correct", "test_edit_user_with_auth", 'test_edit_user_without_auth', 'test_create_order_with_auth_correct',
                             'test_create_order_with_auth_empty', 'test_create_order_with_auth_uncorrect', 'test_get_order_with_auth']:
        delete_user = DeleteUser()
        accessToken = getattr(request.node.cls, 'accessToken', None)
        response = delete_user.delete_user(accessToken)
        assert response.status_code == 202