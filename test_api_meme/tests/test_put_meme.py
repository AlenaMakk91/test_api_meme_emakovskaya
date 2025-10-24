import allure
import pytest

from test_api_meme.test_data.credentional import user2
from test_api_meme.test_data.json_schemas import json_schema_put_meme
from test_api_meme.test_data.payloads_for_put import default_payload, payload_without_text, \
    payload_incorrect_type_for_text, \
    payload_incorrect_type_for_tags, payload_incorrect_type_for_url, payload_without_url, payload_without_tags, \
    payload_without_info, payload_with_empty_body, payload_incorrect_type_for_info


@allure.story('Позитив')
@allure.title('Проверка статус кода 200 в ответе')
def test_put_meme_status_code_200(get_headers, put_meme_endpoint, create_new_meme_id):
    put_meme_endpoint.put_meme(headers=get_headers, payload=default_payload, new_meme_id=create_new_meme_id)
    put_meme_endpoint.check_status_code_is_200()


@allure.story('Позитив')
@allure.title('Проверка схемы json')
def test_put_meme_json_schema(get_headers, put_meme_endpoint, create_new_meme_id):
    put_meme_endpoint.put_meme(headers=get_headers, payload=default_payload, new_meme_id=create_new_meme_id)
    put_meme_endpoint.check_json_schema_in_response(json_schema=json_schema_put_meme)


@allure.story('Позитив')
@allure.title('Проверка в созданном меме параметр text')
def test_put_meme_text_in_response(get_headers, put_meme_endpoint, create_new_meme_id):
    put_meme_endpoint.put_meme(headers=get_headers, payload=default_payload, new_meme_id=create_new_meme_id)
    with allure.step('Проверить в созданном меме параметр text'):
        assert put_meme_endpoint.response_json['text'] == default_payload['text']


@allure.story('Позитив')
@allure.title('Проверка в созданном меме параметр url')
def test_put_meme_url_in_response(get_headers, put_meme_endpoint, create_new_meme_id):
    put_meme_endpoint.put_meme(headers=get_headers, payload=default_payload, new_meme_id=create_new_meme_id)
    with allure.step('Проверить в созданном меме параметр url'):
        assert put_meme_endpoint.response_json['url'] == default_payload['url']


@allure.story('Позитив')
@allure.title('Проверка в созданном меме параметр tags')
def test_put_meme_tags_in_response(get_headers, put_meme_endpoint, create_new_meme_id):
    put_meme_endpoint.put_meme(headers=get_headers, payload=default_payload, new_meme_id=create_new_meme_id)
    with allure.step('Проверить в созданном меме параметр tags'):
        assert put_meme_endpoint.response_json['tags'] == default_payload['tags']


@allure.story('Позитив')
@allure.title('Проверка в созданном меме параметр info')
def test_put_meme_info_in_response(get_headers, put_meme_endpoint, create_new_meme_id):
    put_meme_endpoint.put_meme(headers=get_headers, payload=default_payload, new_meme_id=create_new_meme_id)
    with allure.step('Проверить в созданном меме параметр info'):
        assert put_meme_endpoint.response_json['info'] == default_payload['info']


@allure.story('Негатив')
@allure.title('Тест на обязательность авторизации при выполнении запроса')
def test_put_meme_status_code_without_authorize(put_meme_endpoint, create_new_meme_id):
    put_meme_endpoint.put_meme(headers=None, payload=default_payload, new_meme_id=create_new_meme_id)
    put_meme_endpoint.check_status_code_is_401()


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
def test_put_meme_incorrect_payload(get_headers, put_meme_endpoint, create_new_meme_id, payload):
    put_meme_endpoint.put_meme(headers=get_headers, payload=payload, new_meme_id=create_new_meme_id)
    put_meme_endpoint.check_status_code_is_400()


@allure.story('Негатив')
@allure.title('Тест на ошибку 403 при попытке изменить чужой мем')
def test_put_meme_forbidden(put_meme_endpoint, create_new_meme_id, generate_headers):
    headers = generate_headers.generate_headers(user2)
    put_meme_endpoint.put_meme(headers=headers, payload=default_payload, new_meme_id=create_new_meme_id)
    put_meme_endpoint.check_status_code_is_403()
