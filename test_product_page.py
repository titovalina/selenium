import time

import pytest

from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage


PRODUCT_URL = (
    "http://selenium1py.pythonanywhere.com/en-gb/catalogue/"
    "the-city-and-the-stars_95/"
)


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, PRODUCT_URL)
    page.open()

    product_name = page.get_product_name()
    product_price = page.get_product_price()

    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_success_message(product_name)
    page.should_be_basket_total_equal_to_product_price(
        product_price
    )


@pytest.mark.need_review
def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, PRODUCT_URL)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(
    browser
):
    page = ProductPage(browser, PRODUCT_URL)
    page.open()
    page.go_to_basket_page()

    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_products_in_basket()
    basket_page.should_be_empty_basket_message()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, PRODUCT_URL)
    page.open()
    page.go_to_login_page()

    assert "login" in browser.current_url.lower()


@pytest.mark.need_review
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"
        password = "test_password_123"

        page = LoginPage(
            browser,
            "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        )
        page.open()
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, PRODUCT_URL)
        page.open()

        product_name = page.get_product_name()
        product_price = page.get_product_price()

        page.add_product_to_basket()
        page.solve_quiz_and_get_code()
        page.should_be_success_message(product_name)
        page.should_be_basket_total_equal_to_product_price(
            product_price
        )
