# tests/environment.py

import os
import allure
from allure_commons.types import AttachmentType
from setup_driver import get_driver
from tests.utils.screenshot_utils import ScreenshotUtils


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
    """ Inicializa la carpeta de capturas con el nombre del escenario """
    ScreenshotUtils.initialize_execution_folder(scenario.name)
    url = os.getenv("APP_URL", "http://localhost:3000/login")    # Puedes definir la URL desde env o usar un valor por defecto


    print("Inicializando WebDriver...")  # Debugging
    context.driver = get_driver(browser, headless)
    print("WebDriver inicializado:", context.driver)
    context.driver.get(url)

def after_scenario(context, scenario):
    """ Captura pantalla si el escenario falla y la guarda en la carpeta del escenario. """
    if scenario.status == "failed" and hasattr(context, "driver"):
        try:
            ScreenshotUtils.take_screenshot(context.driver, "failed_scenario")

            # Adjuntar la captura a Allure
            screenshot_path = os.path.join(ScreenshotUtils.execution_folder, "failed_scenario.png")
            with open(screenshot_path, "rb") as image_file:
                allure.attach(image_file.read(), name="failed_scenario", attachment_type=AttachmentType.PNG)

        except Exception as e:
            print(f" Error al capturar pantalla: {e}")

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