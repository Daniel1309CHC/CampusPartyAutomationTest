from selenium.webdriver.common.by import By
from tests.pages.base_page import BasePage

class RegisterPage(BasePage):
    NAME_INPUT = (By.ID, "name")
    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "password")
    CONFIRM_PASSWORD_INPUT = (By.ID, "confirmPassword")
    REGISTER_BUTTON = (By.CSS_SELECTOR, ".register-button")
    DASHBOARD = (By.CSS_SELECTOR, ".dashboard-content")
    REGISTER_LINK = (By.XPATH, "//a[@href='/register']")
    MESSAGE_ERROR = (By.ID, "error_register")

    def fill_registration_form(self, nombre, correo, contrasena, confirmar_contrasena):
        self.wait_for_element(self.NAME_INPUT).send_keys(nombre)
        self.wait_for_element(self.EMAIL_INPUT).send_keys(correo)
        self.wait_for_element(self.PASSWORD_INPUT).send_keys(contrasena)
        self.wait_for_element(self.CONFIRM_PASSWORD_INPUT).send_keys(confirmar_contrasena)

    def submit_registration(self):
        self.wait_for_element(self.REGISTER_BUTTON).click()

    def is_register_error(self):
        return self.is_element_present(self.MESSAGE_ERROR)

    def click_register_link(self):
        self.wait_for_element(self.REGISTER_LINK).click()