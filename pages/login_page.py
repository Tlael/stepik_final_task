import time

from .base_page import BasePage
from selenium.webdriver.common.by import By

from .locators import LoginPageLocators


class LoginPage(BasePage):
    def __init__(self, browser, url):
        super().__init__(browser, url)

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "Login is absent in current url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(By.CSS_SELECTOR, "#login_form"), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(By.CSS_SELECTOR, "#register_form"), "Register_form is not presented"

    def make_email_and_pass(self):
        # генерация почты и передача пароля
        return str(time.time()) + "@fakemail.org", "myStrongPassword№121"

    def register_new_user(self, email, password):
        # регистрация нового пользователя
        self.email = email
        self.password = password

        # находим элементы на странице: поля ввода почты, пароля и кнопку регистрации
        email_input = self.browser.find_element(*LoginPageLocators.EMAIL)
        pass_input = self.browser.find_element(*LoginPageLocators.PASS)
        pass_confirm = self.browser.find_element(*LoginPageLocators.PASS_CHECK)
        reg_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)

        # вводим почту, пароль
        email_input.send_keys(email)
        pass_input.send_keys(password)
        pass_confirm.send_keys(password)

        # нажимаем на кнопку: зарегистрировать
        reg_button.click()
