import requests

class APIAuthPage:
    BASE_URL = "http://localhost:3001"

    def get_auth_token(self):
        """Obtiene el token de autenticación."""
        url = f"{self.BASE_URL}/auth/login"
        payload = {
            "email": "danielchaparro@gmail.com",
            "password": "123"
        }
        # headers = {"Content-Type": "application/json"}

        response = requests.post(url, json=payload)

        if response.status_code == 200:
            return response.json().get("access_token")
        return response.status_code