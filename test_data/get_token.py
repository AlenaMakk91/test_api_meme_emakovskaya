from config import Base_URL

import requests

from test_data.credentional import default_user


class GetToken:

    def __init__(self):
        self.current_token = None

    def generate_token(self, user_name):
        response = requests.post(f"{Base_URL}/authorize", json={"name": user_name})
        response.raise_for_status()
        token = response.json()['token']
        return token

    def is_token_alive(self, token):
        response = requests.get(f"{Base_URL}/authorize/{token}")
        if response.status_code != 200:
            return False
        return True

    def get_authorization(self, user_name=None, current_token=None):
        user_name = user_name if user_name else default_user
        if current_token and self.is_token_alive(current_token):
            return self.current_token
        self.current_token = self.generate_token(user_name)
        return self.current_token

    def generate_headers(self, user_name=None, current_token=None):
        user_name = user_name if user_name else default_user
        self.current_token = self.generate_token(user_name)
        headers = {
            'Authorization': f'{self.current_token}'
        }
        return headers
