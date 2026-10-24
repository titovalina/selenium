import math

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.timeout = timeout

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except Exception:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((how, what))
            )
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until_not(
                EC.presence_of_element_located((how, what))
            )
        except TimeoutException:
            return False
        return True

    def solve_quiz_and_get_code(self):
        alert = WebDriverWait(self.browser, 5).until(
            EC.alert_is_present()
        )
        alert_text = alert.text
        answer = str(math.log(abs(int(alert_text.split()[-1]))))
        alert.send_keys(answer)
        alert.accept()

        try:
            WebDriverWait(self.browser, 5).until(
                EC.alert_is_present()
            )
            self.browser.switch_to.alert.accept()
        except TimeoutException:
            pass

    def go_to_login_page(self):
        self.browser.find_element(
            *BasePageLocators.LOGIN_LINK
        ).click()

    def should_be_login_link(self):
        assert self.is_element_present(
            *BasePageLocators.LOGIN_LINK
        ), "Login link is not presented"

    def go_to_basket_page(self):
        self.browser.find_element(
            *BasePageLocators.BASKET_LINK
        ).click()

    def should_be_authorized_user(self):
        assert self.is_element_present(
            *BasePageLocators.USER_ICON
        ), "User icon is not presented, probably unauthorised user"
