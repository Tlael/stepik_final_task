import math
from selenium.common.exceptions import NoAlertPresentException
from pages.base_page import BasePage
from pages.locators import CartPageLocators, BasketLocators


class ProductPage(BasePage):
    def find_book_name(self):
        return self.browser.find_element(*CartPageLocators.BOOK_NAME).text

    def find_book_in_cart(self):
        return self.browser.find_element(*CartPageLocators.BOOK_TO_COMPARE).text

    def find_price(self):
        return self.browser.find_element(*CartPageLocators.BOOK_PRICE).text

    def find_price_in_cart(self):
        return self.browser.find_element(*CartPageLocators.PRICE_TO_COMPARE).text

    def go_to_cart(self):
        link = self.browser.find_element(*CartPageLocators.CART_LINK)
        link.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def check_product_name(self, bookToCompare, book_in_cart):
        assert book_in_cart == bookToCompare, "FAIL"

    def check_product_price(self, priceToCompare, price_in_cart):
        assert price_in_cart == priceToCompare, "FAIL"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*CartPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def test_guest_cant_see_success_message_after_adding_product_to_basket(self):
        assert self.is_not_element_present(*CartPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def test_guest_cant_see_success_message(self):
        assert self.is_not_element_present(*CartPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def test_message_disappeared_after_adding_product_to_basket(self):
        assert self.is_disappeared(*CartPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def test_empty_cart(self):
        assert self.is_not_element_present(*BasketLocators.EMPTY_CART), \
            "Cart is not empty"

    def test_empty_cart_text(self):
        assert self.browser.find_element(*BasketLocators.EMPTY_CART_TEXT), \
            "Cart is not empty"

    def add_item_to_cart(self):
        addButton = self.browser.find_element(*CartPageLocators.ADD_TO_CART_BUTTON)
        addButton.click()