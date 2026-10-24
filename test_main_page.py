import pytest

from pages.main_page import MainPage
from pages.basket_page import BasketPage


def test_guest_cant_see_product_in_basket_opened_from_main_page(
    browser
):
    page = MainPage(
        browser,
        "http://selenium1py.pythonanywhere.com/"
    )
    page.open()
    page.go_to_basket_page()

    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_products_in_basket()
    basket_page.should_be_empty_basket_message()


@pytest.mark.login_guest
def test_guest_can_go_to_login_page(browser):
    page = MainPage(
        browser,
        "http://selenium1py.pythonanywhere.com/"
    )
    page.open()
    page.go_to_login_page()

    assert "login" in browser.current_url.lower()


@pytest.mark.login_guest
def test_guest_should_see_login_link(browser):
    page = MainPage(
        browser,
        "http://selenium1py.pythonanywhere.com/"
    )
    page.open()
    page.should_be_login_link()
