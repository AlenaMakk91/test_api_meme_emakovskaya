import allure
import requests

from test_api_meme.config import Base_URL
from test_api_meme.endpoints.endpoint import Endpoint


class DeleteMeme(Endpoint):
    @allure.step('Вызов ендпоинта DELETE /meme/<id>')
    def delete_meme(self, headers, new_meme_id):
        self.response = requests.delete(
            url=f'{Base_URL}/meme/{new_meme_id}',
            headers=headers
        )
        with allure.step(f'Ответ вернулся со статус кодом {self.response.status_code}'):
            return self.response
