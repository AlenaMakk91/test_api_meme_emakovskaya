import allure
import pytest

from test_data.json_schemas import json_schema_get_meme_id
from test_data.payloads_for_post import default_post_payload


@pytest.mark.smoke
@allure.story('Позитив')
@allure.title('Проверка статус кода 200 в ответе')
def test_get_meme_status_code(get_headers, create_new_meme_id, get_meme_endpoint):
    get_meme_endpoint.get_meme_id(headers=get_headers, new_meme_id=create_new_meme_id)
    get_meme_endpoint.check_status_code_is_200()
    get_meme_endpoint.check_id_in_response(new_meme_id=create_new_meme_id)


@pytest.mark.regression
@allure.story('Позитив')
@allure.title('Проверка схемы json')
def test_get_meme_id_check_json_schema(get_headers, create_new_meme_id, get_meme_endpoint):
    get_meme_endpoint.get_meme_id(headers=get_headers, new_meme_id=create_new_meme_id)
    get_meme_endpoint.check_json_schema_in_response(json_schema=json_schema_get_meme_id)


@pytest.mark.extended
@allure.story('Позитив')
@allure.title('Проверка в ответе сохраненных параметров')
def test_meme_text_in_response(get_headers, create_new_meme_id, get_meme_endpoint):
    get_meme_endpoint.get_meme_id(headers=get_headers, new_meme_id=create_new_meme_id)
    for parameter in ['text', 'url', 'tags', 'info']:
        get_meme_endpoint.check_parameters_in_response(payload=default_post_payload, parameter=parameter)


@pytest.mark.extended
@allure.story('Негатив')
@allure.title('Тест на обязательность авторизации при выполнении запроса')
def test_get_meme_status_code_without_authorize(get_meme_endpoint, create_new_meme_id):
    get_meme_endpoint.get_meme_id(headers=None, new_meme_id=create_new_meme_id)
    get_meme_endpoint.check_status_code_is_401()


@pytest.mark.smoke
@allure.story('Негатив')
@allure.title('Проверка ошибки 404 если meme не существует в системе')
def test_meme_not_found(get_headers, get_meme_endpoint, create_new_meme_id, delete_meme_endpoint):
    meme_not_exist = create_new_meme_id
    delete_meme_endpoint.delete_meme(headers=get_headers, new_meme_id=meme_not_exist)
    get_meme_endpoint.get_meme_id(headers=get_headers, new_meme_id=meme_not_exist)
    get_meme_endpoint.check_status_code_is_404()
