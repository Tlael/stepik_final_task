import time
import pytest

from pages.locators import LinksLocators
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage


class TestGuestAddToBasketFromProductPage:
    def test_guest_cant_see_success_message(self, browser):
        link = LinksLocators.PRODUCT_PAGE
        page = ProductPage(browser, link)
        page.open()
        page.test_guest_cant_see_success_message()

    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self, browser):
        link = LinksLocators.PRODUCT_PAGE
        page = ProductPage(browser, link)
        page.open()
        page.go_to_cart()
        page.solve_quiz_and_get_code()
        priceToCompare = page.find_price()
        price_in_cart = page.find_price_in_cart()
        bookToCompare = page.find_book_name()
        book_in_cart = page.find_book_in_cart()
        page.check_product_name(bookToCompare, book_in_cart)
        page.check_product_price(priceToCompare, price_in_cart)
        time.sleep(5)


@pytest.mark.logged_user
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = LinksLocators.LOGIN_PAGE
        self.browser = browser
        page = LoginPage(browser, link)
        page.open()
        email, password = page.make_email_and_pass()
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = LinksLocators.PROMO_PAGE
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = LinksLocators.PROMO_PAGE
        page = ProductPage(browser, link)
        page.open()
        page.add_item_to_cart()
        page.solve_quiz_and_get_code()
        priceToCompare = page.find_price()
        price_in_cart = page.find_price_in_cart()
        bookToCompare = page.find_book_name()
        book_in_cart = page.find_book_in_cart()
        page.check_product_name(bookToCompare, book_in_cart)
        page.check_product_price(priceToCompare, price_in_cart)
        time.sleep(5)


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = LinksLocators.PRODUCT_PAGE
    page = ProductPage(browser, link)
    page.open()
    page.go_to_cart()
    page.solve_quiz_and_get_code()
    page.test_guest_cant_see_success_message_after_adding_product_to_basket()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = LinksLocators.PRODUCT_PAGE
    page = ProductPage(browser, link)
    page.open()
    page.go_to_cart()
    page.solve_quiz_and_get_code()
    page.test_message_disappeared_after_adding_product_to_basket()


def test_guest_should_see_login_link_on_product_page(browser):
    link = LinksLocators.PRODUCT_PAGE
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = LinksLocators.MAIN_PAGE
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = LinksLocators.PRODUCT_PAGE
    page = ProductPage(browser, link)
    page.open()
    page.go_to_cart()
    page.test_empty_cart()
    page.test_empty_cart_text()
