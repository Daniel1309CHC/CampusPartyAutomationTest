from behave import given, when, then
from tests.pages.api_users_page import APIUsersPage


@given("que el usuario tiene acceso al token de autenticacion")
def step_get_auth_token(context):
    context.api_users = APIUsersPage()
    context.auth_token = context.api_users.get_auth_token()

    assert context.auth_token is not None, "Error: No se obtuvo el token de autenticación"


@when("envía una solicitud GET al endpoint de usuarios")
def step_send_get_users_request(context):
    context.response = context.api_users.get_users()


@then("la respuesta debe contener los datos de los usuarios")
def step_validate_users_response(context):
    assert context.response is not None, "Error: No se pudo obtener la respuesta"
    assert context.response.status_code == 200, f"Error: Código de estado inesperado {context.response.status_code}"

    users_data = context.response.json()

    assert isinstance(users_data, list), "Error: La respuesta no es una lista de usuarios"
    assert len(users_data) > 0, "Error: No se encontraron usuarios en la respuesta"

    # Validar estructura de un usuario
    expected_keys = {"id", "username", "email", "role"}
    for user in users_data:
        assert expected_keys.issubset(user.keys()), "Error: La estructura del usuario no es la esperada"