from selenium.webdriver.common.by import By


# class MainPageLocators:
#     LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form'),
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class CartPageLocators:
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div")
    CART_LINK = (By.CSS_SELECTOR, '#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a')
    BOOK_NAME = (By.CSS_SELECTOR, ".product_page h1")
    BOOK_TO_COMPARE = (By.CSS_SELECTOR, "div.alertinner strong")
    BOOK_PRICE = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRICE_TO_COMPARE = (By.CSS_SELECTOR, ".product_main p.price_color")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class BasketLocators:
    EMPTY_CART = (By.CSS_SELECTOR, "#content_inner > div.basket-title.hidden-xs > div")
    EMPTY_CART_TEXT = (By.CSS_SELECTOR, "#content_inner > p")
