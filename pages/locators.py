from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form'),
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class CartPageLocators:
    CART_LINK = (By.CSS_SELECTOR, '.add-to-basket .btn, .btn-wishlist')
    BOOK_NAME = (By.CSS_SELECTOR, ".product_page h1")
    BOOK_TO_COMPARE = (By.CSS_SELECTOR, "div.alertinner strong")
    BOOK_PRICE = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRICE_TO_COMPARE = (By.CSS_SELECTOR, ".product_main p.price_color")
