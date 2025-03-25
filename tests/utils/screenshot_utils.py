import os


class ScreenshotUtils:
    execution_folder = None

    @classmethod
    def initialize_execution_folder(cls, scenario_name):
        """ Crea una carpeta con el nombre del escenario en 'reports/' """
        scenario_folder = scenario_name.replace(" ", "_")  # Reemplaza espacios por guiones bajos
        cls.execution_folder = os.path.join("reports", scenario_folder)

        if not os.path.exists(cls.execution_folder):
            os.makedirs(cls.execution_folder)

        print(f"Carpeta creada: {cls.execution_folder}")

    @classmethod
    def take_screenshot(cls, driver, screenshot_name):
        """ Toma una captura de pantalla y la guarda en la carpeta del escenario """
        if cls.execution_folder is None:
            print("Error: La carpeta de ejecución no está inicializada.")
            return

        screenshot_path = os.path.join(cls.execution_folder, f"{screenshot_name}.png")
        driver.save_screenshot(screenshot_path)
        print(f"Captura guardada en: {screenshot_path}")
