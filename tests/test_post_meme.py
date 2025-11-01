import allure
import pytest

from test_data.credentional import default_user
from test_data.json_schemas import json_schema_post_meme
from test_data.payloads_for_post import (
    default_post_payload,
    payload_without_text,
    payload_incorrect_type_for_text,
    payload_incorrect_type_for_tags,
    payload_incorrect_type_for_url,
    payload_without_url,
    payload_without_tags,
    payload_without_info,
    payload_with_empty_body,
    payload_incorrect_type_for_info
)


@allure.story('Позитив')
@allure.title('Проверка схемы json')
def test_post_meme_json_schema(get_headers, post_meme_endpoint):
    post_meme_endpoint.post_meme(headers=get_headers, payload=default_post_payload)
    post_meme_endpoint.check_status_code_is_200()
    post_meme_endpoint.check_json_schema_in_response(json_schema=json_schema_post_meme)


@pytest.mark.parametrize(
    'parameter',
    [
        'text', 'url', 'tags', 'info'
    ]
)
@allure.story('Позитив')
@allure.title('Проверка корректности возвращаемых параметров в ответе')
def test_post_meme_text_in_response(get_headers, post_meme_endpoint, parameter):
    post_meme_endpoint.post_meme(headers=get_headers, payload=default_post_payload)
    post_meme_endpoint.check_parameters_in_response(payload=default_post_payload, parameter=parameter)


@allure.story('Позитив')
@allure.title('Проверка значения updated_by в ответе')
def test_post_meme_info_in_response(get_headers, post_meme_endpoint):
    post_meme_endpoint.post_meme(headers=get_headers, payload=default_post_payload)
    post_meme_endpoint.check_updated_by_in_response(default_user)


@allure.story('Негатив')
@allure.title('Тест на обязательность авторизации при выполнении запроса')
def test_post_meme_status_code_without_authorize(post_meme_endpoint):
    post_meme_endpoint.post_meme(headers=None, payload=default_post_payload)
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
    post_meme_endpoint.check_status_code_is_400()
