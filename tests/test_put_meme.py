import copy

import allure
import pytest

from test_data.credentional import user2, default_user
from test_data.json_schemas import json_schema_put_meme
from test_data.payloads_for_post import (
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
from test_data.payloads_for_put import default_put_payload


@allure.story('Позитив')
@allure.title('Проверка схемы json')
def test_put_meme_json_schema(get_headers, put_meme_endpoint, create_new_meme_id):
    payload = copy.deepcopy(default_put_payload)
    put_meme_endpoint.put_meme(headers=get_headers, payload=payload, new_meme_id=create_new_meme_id)
    put_meme_endpoint.check_status_code_is_200()
    put_meme_endpoint.check_json_schema_in_response(json_schema=json_schema_put_meme)


@allure.story('Позитив')
@allure.title('Проверка в ответе параметра updated_by')
def test_put_meme_text_in_response(get_headers, put_meme_endpoint, create_new_meme_id):
    payload = copy.deepcopy(default_put_payload)
    put_meme_endpoint.put_meme(headers=get_headers, payload=payload, new_meme_id=create_new_meme_id)
    put_meme_endpoint.check_updated_by_in_response(user=default_user)


@pytest.mark.parametrize(
    'parameter',
    [
        'text', 'url', 'tags', 'info'
    ]
)
@allure.story('Позитив')
@allure.title('Проверить что в ответе возвращаются верные параметры')
def test_parameters_in_response(get_headers, put_meme_endpoint, create_new_meme_id, parameter):
    payload = copy.deepcopy(default_put_payload)
    put_meme_endpoint.put_meme(headers=get_headers, payload=payload, new_meme_id=create_new_meme_id)
    put_meme_endpoint.check_parameters_in_response(parameter=parameter, payload=payload)


@pytest.mark.parametrize(
    'parameter',
    [
        'text', 'url', 'tags', 'info'
    ]
)
@allure.story('Позитив')
@allure.title('Проверка сохранения мема с пустыми параметрами')
def test_update_meme_with_empty_parameters(get_headers, create_new_meme_id, parameter, put_meme_endpoint):
    payload = copy.deepcopy(default_put_payload)
    payload[f'{parameter}'] = ""
    put_meme_endpoint.put_meme(headers=get_headers, new_meme_id=create_new_meme_id, payload=payload)
    put_meme_endpoint.check_parameters_in_response(parameter=parameter, payload=payload)


@allure.story('Негатив')
@allure.title('Тест на обязательность авторизации при выполнении запроса')
def test_put_meme_status_code_without_authorize(put_meme_endpoint, create_new_meme_id):
    payload = copy.deepcopy(default_put_payload)
    put_meme_endpoint.put_meme(headers=None, payload=payload, new_meme_id=create_new_meme_id)
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
    payload = copy.deepcopy(payload)
    put_meme_endpoint.put_meme(headers=get_headers, payload=payload, new_meme_id=create_new_meme_id)
    put_meme_endpoint.check_status_code_is_400()


@allure.story('Негатив')
@allure.title('Тест на ошибку 403 при попытке изменить чужой мем')
def test_put_meme_forbidden(put_meme_endpoint, create_new_meme_id, generate_headers):
    payload = copy.deepcopy(default_put_payload)
    headers = generate_headers.generate_headers(user2)
    put_meme_endpoint.put_meme(headers=headers, payload=payload, new_meme_id=create_new_meme_id)
    put_meme_endpoint.check_status_code_is_403()
