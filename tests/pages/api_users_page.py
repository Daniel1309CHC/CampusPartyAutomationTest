import pdb

import requests

from tests.pages.api_auth_page import APIAuthPage


class APIUsersPage:
    BASE_URL = "http://localhost:3001"

    def __init__(self):
        self.auth = APIAuthPage()  # Instanciamos la autenticación

    def get_auth_token(self):
        """Obtiene el token llamando a la APIAuthPage."""
        return self.auth.get_auth_token()

    def get_users(self):
        """Obtiene la lista de usuarios con un token válido."""
        token = self.get_auth_token()

        if not token:
            return None  # Si no hay token, devolvemos None

        url = f"{self.BASE_URL}/auth/all"
        headers = {"Authorization": f"Bearer {token}"}

        return requests.get(url, headers=headers)