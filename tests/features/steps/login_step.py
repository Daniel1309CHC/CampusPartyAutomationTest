from behave import given, when, then
from tests.pages.login_page import LoginPage
from tests.utils.screenshot_utils import ScreenshotUtils


@given("el usuario está en la página de inicio de sesión")
def step_open_login_page(context):
    context.login_page = LoginPage(context.driver)
    # Toma captura con nombre "step_login"
    ScreenshotUtils.take_screenshot(context.driver, "step_login")

@when('ingresa su correo "{email}" y contraseña "{password}"')
def step_enter_credentials(context, email, password):
    context.login_page.enter_email(email)
    context.login_page.enter_password(password)
    context.login_page.click_login()

@then("el usuario debe acceder correctamente al sistema")
def step_verify_login(context):
    assert context.login_page.is_logged_in(), "Error: No se pudo iniciar sesión correctamente"