import allure

from test_api_meme.config import Base_URL
from test_api_meme.test_data.json_schemas import json_schema_get_meme_id
from test_api_meme.test_data.payloads_for_post import default_payload


@allure.story('Позитив')
@allure.title('Проверка статус кода 200 в ответе')
def test_get_meme_status_code(get_headers, create_new_meme_id, get_meme_endpoint):
    get_meme_endpoint.get_meme_id(headers=get_headers, new_meme_id=create_new_meme_id)
    get_meme_endpoint.check_status_code_is_200()


@allure.story('Позитив')
@allure.title('Проверка схемы json')
def test_get_meme_id_check_json_schema(get_headers, create_new_meme_id, get_meme_endpoint):
    get_meme_endpoint.get_meme_id(headers=get_headers, new_meme_id=create_new_meme_id)
    get_meme_endpoint.check_json_schema_in_response(json_schema=json_schema_get_meme_id)


@allure.story('Негатив')
@allure.title('Тест на обязательность авторизации при выполнении запроса')
def test_new_meme_in_response(get_headers, create_new_meme_id, get_meme_endpoint):
    get_meme_endpoint.get_meme_id(headers=get_headers, new_meme_id=create_new_meme_id)


@allure.story('Позитив')
@allure.title('Проверка в созданном меме параметр text')
def test_meme_text_in_response(get_headers, create_new_meme_id, get_meme_endpoint):
    get_meme_endpoint.get_meme_id(headers=get_headers, new_meme_id=create_new_meme_id)
    with allure.step('Проверить в созданном меме параметр text'):
        assert get_meme_endpoint.response_json['text'] == default_payload['text']


@allure.story('Позитив')
@allure.title('Проверка в созданном меме параметр url')
def test_meme_url_in_response(get_headers, create_new_meme_id, get_meme_endpoint):
    get_meme_endpoint.get_meme_id(headers=get_headers, new_meme_id=create_new_meme_id)
    with allure.step('Проверить в созданном меме параметр url'):
        assert get_meme_endpoint.response_json['url'] == default_payload['url']


@allure.story('Позитив')
@allure.title('Проверка в созданном меме параметр tags')
def test_meme_tags_in_response(get_headers, create_new_meme_id, get_meme_endpoint):
    get_meme_endpoint.get_meme_id(headers=get_headers, new_meme_id=create_new_meme_id)
    with allure.step('Проверить в созданном меме параметр tags'):
        assert get_meme_endpoint.response_json['tags'] == default_payload['tags']


@allure.story('Позитив')
@allure.title('Проверка в созданном меме параметр info')
def test_meme_info_in_response(get_headers, create_new_meme_id, get_meme_endpoint):
    get_meme_endpoint.get_meme_id(headers=get_headers, new_meme_id=create_new_meme_id)
    with allure.step('Проверить в созданном меме параметр info'):
        assert get_meme_endpoint.response_json['info'] == default_payload['info']


@allure.story('Негатив')
@allure.title('Тест на обязательность авторизации при выполнении запроса')
def test_get_meme_status_code_without_authorize(get_meme_endpoint, create_new_meme_id):
    get_meme_endpoint.get_meme_id(headers=None, new_meme_id=create_new_meme_id)
    get_meme_endpoint.check_status_code_is_401()


@allure.story('Негатив')
@allure.title('Проверка ошибки 404 если meme не существует в системе')
def test_meme_not_found(get_headers, get_meme_endpoint):
    get_meme_endpoint.get_meme_id(headers=get_headers, new_meme_id=123456789)
    get_meme_endpoint.check_status_code_is_404()
