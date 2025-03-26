from behave import given, when, then
from tests.pages.login_page import LoginPage
from tests.pages.registro_page import RegisterPage

from tests.utils.screenshot_utils import ScreenshotUtils
import time


@given("que el usuario accede al registro desde la pantalla de inicio")
def step_user_navigates_to_register(context):
    context.login_page = LoginPage(context.driver)
    context.register_page = RegisterPage(context.driver)
    context.register_page.click_register_link()



@when("llena el formulario de registro con informacion valida")
def step_fill_registration_form(context):
    context.register_page.fill_registration_form(
        nombre="Juan Perez",
        correo="juan.perez@correo.com",
        contrasena="Pass1234",
        confirmar_contrasena="Pass1234"
    )
    ScreenshotUtils.take_screenshot(context.driver, "formulario_completado")
    context.register_page.submit_registration()


@then("accede al dashboard de inicio de campus party")
def step_validate_dashboard_access(context):
    time.sleep(3)  # Esperar redirección
    ScreenshotUtils.take_screenshot(context.driver, "dashboard_acceso")

    assert context.register_page.is_logged_in(), "Error: No se redirigió al dashboard"


@when("intenta registrarse con un correo ya registrado")
def step_fill_registration_form_invalid(context):
    context.register_page.fill_registration_form(
        nombre="Juan Perez",
        correo="juan.perez@correo.com",
        contrasena="Pass1234",
        confirmar_contrasena="Pass1234"
    )
    ScreenshotUtils.take_screenshot(context.driver, "formulario_completado")
    context.register_page.submit_registration()


@then("recibe un mensaje de error indicando que el usuario ya existe")
def step_validate_access(context):
    time.sleep(3)  # Esperar redirección
    ScreenshotUtils.take_screenshot(context.driver, "Mensaje de error")

    assert context.register_page.is_register_error(), "Error: No se visualiza mensaje de usuario ya registrado"