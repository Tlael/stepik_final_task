import time

from pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
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
