import allure

from config import Base_URL
from test_data.json_schemas import json_schema_get_memes


@allure.story('Позитив')
@allure.title('Проверка схемы json')
def test_get_memes_json_schema_validate(get_headers, get_memes_endpoint):
    get_memes_endpoint.get_meme(headers=get_headers)
    get_memes_endpoint.check_status_code_is_200()
    get_memes_endpoint.check_json_schema_in_response(json_schema=json_schema_get_memes)


@allure.story('Негатив')
@allure.title('Тест на обязательность авторизации при выполнении запроса')
def test_get_memes_status_code_without_authorize(get_memes_endpoint):
    get_memes_endpoint.get_meme(headers=None)
    get_memes_endpoint.check_status_code_is_401()


@allure.story('Негатив')
@allure.title('Проверка ошибки 404')
def test_page_not_found(get_headers, get_memes_endpoint):
    get_memes_endpoint.get_meme_with_custom_params(headers=get_headers, url=f'{Base_URL}/memesssss')
    get_memes_endpoint.check_status_code_is_404()
