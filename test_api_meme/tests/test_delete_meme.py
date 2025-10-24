import allure

from test_api_meme.test_data.credentional import user2


@allure.story('Позитив')
@allure.title('Проверка статус кода 200 в ответе')
def test_delete_meme_status_code(get_headers, delete_meme_endpoint, create_new_meme_id):
    delete_meme_endpoint.delete_meme(headers=get_headers, new_meme_id=create_new_meme_id)
    delete_meme_endpoint.check_status_code_is_200()


@allure.story('Негатив')
@allure.title('Тест на обязательность авторизации при выполнении запроса')
def test_delete_meme_status_code_without_authorize(delete_meme_endpoint, create_new_meme_id):
    delete_meme_endpoint.delete_meme(headers=None, new_meme_id=create_new_meme_id)
    delete_meme_endpoint.check_status_code_is_401()


@allure.story('Негатив')
@allure.title('Тест на ошибку 403 при попытке удалить чужой мем')
def test_delete_meme_forbidden(get_headers, delete_meme_endpoint, create_new_meme_id, generate_headers):
    headers = generate_headers.generate_headers(user2)
    delete_meme_endpoint.delete_meme(headers=headers, new_meme_id=create_new_meme_id)
    delete_meme_endpoint.check_status_code_is_403()


@allure.story('Негатив')
@allure.title('Проверка ошибки 404 если meme не существует в системе')
def test_delete_meme_not_found(get_headers, delete_meme_endpoint):
    delete_meme_endpoint.delete_meme(headers=get_headers, new_meme_id=123456789)
    delete_meme_endpoint.check_status_code_is_404()
