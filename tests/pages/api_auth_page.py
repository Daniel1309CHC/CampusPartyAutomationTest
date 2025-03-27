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
        headers = {"Content-Type": "application/json"}

        response = requests.post(url, json=payload)

        if response.status_code == 201:
            return response.json().get("access_token")
        return response.status_code

    def login(self, credentials):
        """Envía una solicitud POST para autenticar al usuario y obtener un token."""
        url = f"{self.BASE_URL}/auth/login"

        response = requests.post(url, json=credentials)

        if response.status_code == 201:  # Verifica que la autenticación fue exitosa
            data = response.json()  # Convierte la respuesta a JSON
            return data.get("access_token"), data  # Retorna el token y los datos completos del usuario

        return None, None  # En caso de fallo, retorna valores nulos


    def login_invalid(self, credentials):
        """
        Envía una solicitud POST con credenciales inválidas y retorna la respuesta completa.
        """
        url = f"{self.BASE_URL}/auth/login"
        response = requests.post(url, json=credentials)
        return response