from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.browser.find_element(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON
        ).click()

    def get_product_name(self):
        return self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME
        ).text

    def get_product_price(self):
        return self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE
        ).text

    def should_be_success_message(self, product_name=None):
        assert self.is_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE
        ), "Success message is not presented"

        message = self.browser.find_element(
            *ProductPageLocators.SUCCESS_MESSAGE
        ).text

        if product_name:
            assert product_name in message, (
                "Product name is not in success message"
            )

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE
        ), "Success message is presented, but should not be"

    def should_be_basket_total_equal_to_product_price(
        self, product_price
    ):
        basket_total = self.browser.find_element(
            *ProductPageLocators.BASKET_TOTAL
        ).text

        assert product_price in basket_total, (
            f"Basket total {basket_total} does not match "
            f"product price {product_price}"
        )
