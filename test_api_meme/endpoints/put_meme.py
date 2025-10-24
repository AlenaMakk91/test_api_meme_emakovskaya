import logging

import allure
import requests

from test_api_meme.config import Base_URL
from test_api_meme.endpoints.endpoint import Endpoint


class PutMeme(Endpoint):
    @allure.step('Вызов ендпоинта PUT /meme/<id>')
    def put_meme(self, headers, payload, new_meme_id):
        payload['id'] = new_meme_id
        self.response = requests.put(
            url=f'{Base_URL}/meme/{new_meme_id}',
            headers=headers,
            json=payload
        )
        with allure.step('Сохранение респонса в формате json'):
            try:
                self.response_json = self.response.json()
            except Exception:
                self.response_json = None
                logging.warning('Не удалось сохранить ответ в json формат')
            with allure.step(f'Ответ вернулся со статус кодом {self.response.status_code}'):
                return self.response
