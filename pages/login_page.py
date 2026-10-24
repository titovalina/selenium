from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        self.browser.find_element(
            *LoginPageLocators.REGISTRATION_EMAIL
        ).send_keys(email)

        self.browser.find_element(
            *LoginPageLocators.REGISTRATION_PASSWORD
        ).send_keys(password)

        self.browser.find_element(
            *LoginPageLocators.REGISTRATION_PASSWORD_CONFIRM
        ).send_keys(password)

        self.browser.find_element(
            *LoginPageLocators.REGISTRATION_SUBMIT
        ).click()
