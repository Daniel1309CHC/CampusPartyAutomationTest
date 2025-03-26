from selenium.webdriver.common.by import By
from tests.pages.base_page import BasePage


class LoginPage(BasePage):
    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".login-button")
    DASHBOARD = (By.CSS_SELECTOR, ".dashboard-content")


    def enter_email(self, email):
        email_input = self.wait_for_element(self.EMAIL_INPUT)
        if not email:  # Verifica si email es None o un string vacío
            email_input.click()
        else:
            email_input.send_keys(email)

    def enter_password(self, password):
        password_input = self.wait_for_element(self.PASSWORD_INPUT)
        if not password:  # Verifica si password es None o un string vacío
            password_input.click()
        else:
            password_input.send_keys(password)

    def click_login(self):
        self.wait_for_element(self.LOGIN_BUTTON).click()

    def is_logged_in(self):
        return self.is_element_present(self.DASHBOARD)