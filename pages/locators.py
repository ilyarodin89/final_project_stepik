from selenium.webdriver.common.by import By


class MainPageLocators():
    """локаторы для MainPage"""
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators(object):
    """локаторы для MainPage"""
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")