from .base_page import BasePage
from .locators import LoginPageLocators
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "подстрока login отсутствует в url браузера"

    def should_be_login_form(self):
        assert self.browser.is_element_present(*LoginPageLocators.LOGIN_FORM), "LOGIN_FORM is not presented"

    def should_be_register_form(self):
        assert self.browser.is_element_present(*LoginPageLocators.REGISTER_FORM), "REGISTER_FORM is not presented"

    def register_new_user(self):
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        input_email = self.browser.find_element(*LoginPageLocators.REGISTR_INPUT_EMAIL)
        input_email.send_keys(email)
        input_password = self.browser.find_element(*LoginPageLocators.REGISTR_INPUT_PASSWORD_1)
        input_password.send_keys(password)
        input_password_2 = self.browser.find_element(*LoginPageLocators.REGISTR_INPUT_PASSWORD_2)
        input_password_2.send_keys(password)
        button_registr_submit = self.browser.find_element(*LoginPageLocators.REGISTR_SUBMIT_BUTTON)
        button_registr_submit.click()
