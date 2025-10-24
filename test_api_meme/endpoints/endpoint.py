import allure
from jsonschema import validate, ValidationError


class Endpoint:
    response = None
    response_json = None
    new_meme_id = None

    @allure.step('Проверить ответ на статус код 200')
    def check_status_code_is_200(self):
        assert self.response.status_code == 200

    @allure.step('Проверить корректность схемы json')
    def check_json_schema_in_response(self, json_schema):
        response_json = self.response_json
        try:
            validate(instance=response_json, schema=json_schema)
        except ValidationError:
            raise AssertionError('Ошибка валидации схемы json')

    @allure.step('Проверить ответ на статус код 404')
    def check_status_code_is_404(self):
        assert self.response.status_code == 404

    @allure.step('Проверить ответ на статус код 401')
    def check_status_code_is_401(self):
        assert self.response.status_code == 401

    @allure.step('Проверить ответ на статус код 400')
    def check_status_code_is_400(self):
        assert self.response.status_code == 400

    @allure.step('Проверить ответ на статус код 403')
    def check_status_code_is_403(self):
        assert self.response.status_code == 403
