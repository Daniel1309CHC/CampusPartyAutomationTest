# tests/environment.py

import os
import allure
from allure_commons.types import AttachmentType
from setup_driver import get_driver


def before_all(context):
    """
    Se ejecuta antes de todas las pruebas.
    Configura el directorio de reportes para Allure.
    """
    context.allure_report_dir = "reports"  # Asegurar que los reportes vayan al directorio correcto
    if not os.path.exists(context.allure_report_dir):
        os.makedirs(context.allure_report_dir)



def before_scenario(context, scenario):
    """
    Se ejecuta antes de cada escenario de Behave.
    """
    # Lee el navegador y el modo headless desde variables de entorno, con valores por defecto.
    browser = os.getenv("BROWSER", "chrome")      # Por defecto: "chrome"
    headless = os.getenv("HEADLESS", "False") == "True"  # Por defecto: False (en formato string)
    url = os.getenv("APP_URL", "https://www.google.com")    # Puedes definir la URL desde env o usar un valor por defecto

    print("Inicializando WebDriver...")  # Debugging
    context.driver = get_driver(browser, headless)
    print("WebDriver inicializado:", context.driver)
    context.driver.get(url)

def after_scenario(context, scenario):
    """
    Se ejecuta después de cada escenario.
    """
    context.driver.quit()

def after_step(context, step):
    """
    Captura pantallazos si un step falla y lo adjunta a Allure.
    """
    if step.status == 'failed':
        allure.attach(
            context.driver.get_screenshot_as_png(),
            name="failed_screenshot",
            attachment_type=AttachmentType.PNG
        )