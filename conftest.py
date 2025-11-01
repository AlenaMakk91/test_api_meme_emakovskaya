import allure
import requests
import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from config import Base_URL
from endpoints.delete_meme import DeleteMeme
from endpoints.get_meme_id import GetMeme
from endpoints.get_meme import GetMemes
from endpoints.post_meme import PostMeme
from endpoints.put_meme import PutMeme
from test_data.get_token import GetToken
from test_data.payloads_for_post import default_post_payload


@pytest.fixture(scope="session")
@allure.title('Подготовка headers с токеном авторизации')
def get_headers():
    token_manager = GetToken()
    token = token_manager.get_authorization()
    headers = {
        'Authorization': f'{token}'
    }
    return headers


@allure.title('Подготовка headers с новым токеном для пользователя')
@pytest.fixture()
def generate_headers():
    return GetToken()


@allure.title('Формирование ендпоинта для вызова')
@pytest.fixture()
def get_memes_endpoint():
    return GetMemes()


@allure.title('Подготовка нового мема')
@pytest.fixture()
def create_new_meme_id(get_headers):
    payload = default_post_payload
    response = requests.post(
        url=f'{Base_URL}/meme',
        json=payload,
        headers=get_headers
    ).json()
    new_meme_id = response['id']
    yield new_meme_id
    with allure.step(f'Удаление мема с id {new_meme_id}'):
        requests.delete(url=f'{Base_URL}/meme/{new_meme_id}', headers=get_headers)


@allure.title('Формирование ендпоинта для вызова')
@pytest.fixture()
def get_meme_endpoint():
    return GetMeme()


@allure.title('Формирование ендпоинта для вызова')
@pytest.fixture()
def post_meme_endpoint():
    return PostMeme()


@allure.title('Формирование ендпоинта для вызова')
@pytest.fixture()
def put_meme_endpoint():
    return PutMeme()


@allure.title('Формирование ендпоинта для вызова')
@pytest.fixture()
def delete_meme_endpoint():
    return DeleteMeme()
