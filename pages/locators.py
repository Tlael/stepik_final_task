from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form'),
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    PASS = (By.CSS_SELECTOR, "#id_registration-password1")
    PASS_CHECK = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form > button")


class CartPageLocators:
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div")
    CART_LINK = (By.CSS_SELECTOR, '#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > '
                                  'span > a')
    BOOK_NAME = (By.CSS_SELECTOR, ".product_page h1")
    BOOK_TO_COMPARE = (By.CSS_SELECTOR, "div.alertinner strong")
    BOOK_PRICE = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRICE_TO_COMPARE = (By.CSS_SELECTOR, ".product_main p.price_color")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form > button")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketLocators:
    EMPTY_CART = (By.CSS_SELECTOR, "#content_inner > div.basket-title.hidden-xs > div")
    EMPTY_CART_TEXT = (By.CSS_SELECTOR, "#content_inner > p")
