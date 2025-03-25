from selenium.webdriver.common.by import By
from tests.pages.base_page import BasePage


class LoginPage(BasePage):
    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    DASHBOARD = (By.ID, "dashboard")


    def enter_email(self, email):
        self.wait_for_element(self.EMAIL_INPUT).send_keys(email)

    def enter_password(self, password):
        self.wait_for_element(self.PASSWORD_INPUT).send_keys(password)

    def click_login(self):
        self.wait_for_element(self.LOGIN_BUTTON).click()

    def is_logged_in(self):
        return self.is_element_present(self.DASHBOARD)