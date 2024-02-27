class Urls:
    # base_url
    base_url = 'https://stellarburgers.nomoreparties.site'
    # create_user
    post_create_user = '/api/auth/register'
    # auth_user
    post_auth_user = '/api/auth/login'
    # edit_user
    get_edit_user = '/api/auth/user'
    patch_edit_user = '/api/auth/user'
    # delete_user
    delete_user = '/api/auth/user'
    # get_ingredients
    get_ingredients = '/api/ingredients'
    # create_order
    post_create_order = '/api/orders'
    get_order = '/api/orders'

class Fields:
    # применяются в test_create_user.py
    empty_email = ['', 'dasdasdas', 'sdasdada']
    empty_password = ['dasdasdas', '', 'asdadasdad']
    empty_name = ['asdasdasd', 'sasasdasd', '']
    error_data = 'Email, password and name are required fields'
