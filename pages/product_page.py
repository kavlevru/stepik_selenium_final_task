from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoSuchElementException


class ProductPage(BasePage):
    product_name = ''
    product_price = 0.00

    def product_add_to_cart(self):
        self.get_product_name()
        self.get_product_price()
        self.click_add_to_cart_button()

    def click_add_to_cart_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BUTTON), 'Add to cart button not found on page'
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()

    def get_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), 'Product name not found on the product page'
        self.product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), 'Product price not found on the product page'
        self.product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_be_message_of_add_product_to_cart(self):
        assert self.is_element_present(*ProductPageLocators.CART_PRODUCT_NAME), 'Add to cart messages not found on the product page'
        cart_product_name = self.browser.find_element(*ProductPageLocators.CART_PRODUCT_NAME).text
        assert self.product_name in cart_product_name, 'Product name in cart not match with product name on page'

    def should_be_cart_price_equal_price_of_product(self):
        assert self.is_element_present(*ProductPageLocators.CART_PRICE), 'Price of cart not found on a product page'
        cart_price = self.browser.find_element(*ProductPageLocators.CART_PRICE).text
        assert cart_price == self.product_price, 'Price in cart not equal product price'

