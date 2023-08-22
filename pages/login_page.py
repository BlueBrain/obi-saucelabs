import time
from locators.login_locators import LoginPageLocators
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import CustomBasePage


class LoginPage(CustomBasePage):
    def __init__(self, browser, wait):
        super().__init__(browser, wait)

    def navigate_to_homepage(self):
        self.browser.get("https://bbp.epfl.ch/mmb-beta")

    def find_login_button(self):
        return self.wait.until(EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON))

    def login(self):
        self.wait.until(EC.presence_of_element_located(LoginPageLocators.USERNAME))
        self.wait.until(EC.presence_of_element_located(LoginPageLocators.PASSWORD))

    def wait_for_login_complete(self):
        """Wait for login to complete by checking URL change"""
        self.wait.until(EC.url_contains("mmb-beta"))

    def find_username_field(self):
        return self.wait.until(EC.presence_of_element_located(LoginPageLocators.USERNAME))

    def find_password_field(self):
        return self.wait.until(EC.presence_of_element_located(LoginPageLocators.PASSWORD))

    def find_signin_button(self):
        return self.wait.until(EC.element_to_be_clickable(LoginPageLocators.SIGN_IN))

    def find_logout_button(self):
        return self.wait.until(EC.element_to_be_clickable(LoginPageLocators.LOGOUT))
