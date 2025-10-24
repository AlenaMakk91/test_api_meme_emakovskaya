import allure
import pytest

from test_api_meme.test_data.json_schemas import json_schema_post_meme
from test_api_meme.test_data.payloads_for_post import default_payload, payload_without_text, \
    payload_incorrect_type_for_text, \
    payload_incorrect_type_for_tags, payload_incorrect_type_for_url, payload_without_url, payload_without_tags, \
    payload_without_info, payload_with_empty_body, payload_incorrect_type_for_info


@allure.story('Позитив')
@allure.title('Проверка статус кода 200 в ответе')
def test_post_meme_status_code_200(get_headers, post_meme_endpoint):
    post_meme_endpoint.post_meme(headers=get_headers, payload=default_payload)
    post_meme_endpoint.check_status_code_is_200()


@allure.story('Позитив')
@allure.title('Проверка схемы json')
def test_post_meme_json_schema(get_headers, post_meme_endpoint):
    post_meme_endpoint.post_meme(headers=get_headers, payload=default_payload)
    post_meme_endpoint.check_json_schema_in_response(json_schema=json_schema_post_meme)


@allure.story('Позитив')
@allure.title('Проверка в созданном меме параметр text')
def test_post_meme_text_in_response(get_headers, post_meme_endpoint):
    post_meme_endpoint.post_meme(headers=get_headers, payload=default_payload)
    with allure.step('Проверить в созданном меме параметр text'):
        assert post_meme_endpoint.response_json['text'] == default_payload['text']


@allure.story('Позитив')
@allure.title('Проверка в созданном меме параметр url')
def test_post_meme_url_in_response(get_headers, post_meme_endpoint):
    post_meme_endpoint.post_meme(headers=get_headers, payload=default_payload)
    with allure.step('Проверить в созданном меме параметр url'):
        assert post_meme_endpoint.response_json['url'] == default_payload['url']


@allure.story('Позитив')
@allure.title('Проверка в созданном меме параметр tags')
def test_post_meme_tags_in_response(get_headers, post_meme_endpoint):
    post_meme_endpoint.post_meme(headers=get_headers, payload=default_payload)
    with allure.step('Проверить в созданном меме параметр tags'):
        assert post_meme_endpoint.response_json['tags'] == default_payload['tags']


@allure.story('Позитив')
@allure.title('Проверка в созданном меме параметр info')
def test_post_meme_info_in_response(get_headers, post_meme_endpoint):
    post_meme_endpoint.post_meme(headers=get_headers, payload=default_payload)
    with allure.step('Проверить в созданном меме параметр info'):
        assert post_meme_endpoint.response_json['info'] == default_payload['info']


@allure.story('Негатив')
@allure.title('Тест на обязательность авторизации при выполнении запроса')
def test_post_meme_status_code_without_authorize(post_meme_endpoint):
    post_meme_endpoint.post_meme(headers=None, payload=default_payload)
    post_meme_endpoint.check_status_code_is_401()


@pytest.mark.parametrize(
    'payload',
    [
        payload_without_text, payload_without_url, payload_without_tags, payload_without_info, payload_with_empty_body,
        payload_incorrect_type_for_text, payload_incorrect_type_for_tags, payload_incorrect_type_for_url,
        payload_incorrect_type_for_info
    ]
)
@allure.story('Негатив')
@allure.title('Тест на ошибку клиента при формировании некорректного body')
def test_post_meme_incorrect_payload(get_headers, post_meme_endpoint, payload):
    post_meme_endpoint.post_meme(headers=get_headers, payload=payload)
