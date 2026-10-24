from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (
        By.CSS_SELECTOR,
        "button.btn-add-to-basket"
    )
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
    BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info strong")


class BasketPageLocators:
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")


class LoginPageLocators:
    REGISTRATION_EMAIL = (
        By.CSS_SELECTOR,
        "#id_registration-email"
    )
    REGISTRATION_PASSWORD = (
        By.CSS_SELECTOR,
        "#id_registration-password1"
    )
    REGISTRATION_PASSWORD_CONFIRM = (
        By.CSS_SELECTOR,
        "#id_registration-password2"
    )
    REGISTRATION_SUBMIT = (
        By.CSS_SELECTOR,
        "#register_form button[name='registration_submit']"
    )
