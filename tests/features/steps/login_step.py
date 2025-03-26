from behave import given, when, then
from tests.pages.login_page import LoginPage
from tests.utils.screenshot_utils import ScreenshotUtils
import pdb

@given("el usuario está en la página de inicio de sesión")
def step_open_login_page(context):
    context.login_page = LoginPage(context.driver)
    # Toma captura con nombre "step_login"
    ScreenshotUtils.take_screenshot(context.driver, "step_login")

@when('ingresa su correo "{email}" y contraseña "{password}"')
def step_enter_credentials(context, email, password):
    if email == ".":
        email = ""
    if password == ".":
        password = ""
    context.login_page.enter_email(email)
    context.login_page.enter_password(password)
    context.login_page.click_login()
    ScreenshotUtils.take_screenshot(context.driver, "Ingreso de credenciales")

@then("el usuario debe acceder correctamente al sistema")
def step_verify_login(context):
    ScreenshotUtils.take_screenshot(context.driver, "acceso al sistema")
    assert context.login_page.is_logged_in(), "Error: No se pudo iniciar sesión correctamente"


@then("el usuario no puede acceder al sistema")
def step_verify_no_access(context):
    ScreenshotUtils.take_screenshot(context.driver, "intento_fallido")
    assert not context.login_page.is_logged_in(), "Error: El usuario pudo acceder con credenciales inválidas"