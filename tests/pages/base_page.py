from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Espera máxima de 10s

    def wait_for_element(self, locator):
        """Esperar y obtener un elemento"""
        return self.wait.until(EC.presence_of_element_located(locator))

    def is_element_present(self, locator):
        """Verificar si un elemento está presente"""
        try:
            self.wait.until(EC.presence_of_element_located(locator))
            return True
        except:
            return False