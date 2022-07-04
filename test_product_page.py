from .pages.product_page import ProductPage
import time

def test_guest_can_add_product_to_basket(browser):
    # link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    page = ProductPage(browser, link)
    page.open()
    page.product_add_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_message_of_add_product_to_cart()
    page.should_be_cart_price_equal_price_of_product()
