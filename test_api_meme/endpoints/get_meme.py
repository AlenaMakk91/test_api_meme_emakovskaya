import logging

import allure
import requests

from test_api_meme.config import Base_URL
from test_api_meme.endpoints.endpoint import Endpoint


class GetMemes(Endpoint):
    @allure.step('Вызов ендпоинта GET /meme')
    def get_meme(self, headers):
        self.response = requests.get(
            url=f'{Base_URL}/meme',
            headers=headers
        )
        with allure.step('Сохранение респонса в формате json'):
            try:
                self.response_json = self.response.json()
            except Exception:
                self.response_json = None
                logging.warning('Не удалось сохранить ответ в json формат')
            with allure.step(f'Ответ вернулся со статус кодом {self.response.status_code}'):
                return self.response

    @allure.step('Вызов ендпоинта GET /meme')
    def get_meme_with_custom_params(self, headers, url):
        self.response = requests.get(
            url=url,
            headers=headers
        )
        with allure.step('Сохранение респонса в формате json'):
            try:
                self.response_json = self.response.json()
            except Exception:
                self.response_json = None
                logging.warning('Не удалось сохранить ответ в json формат')
            with allure.step(f'Ответ вернулся со статус кодом {self.response.status_code}'):
                return self.response
