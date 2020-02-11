from selenium.webdriver.common.by import By


class MainPageLocators():
    """локаторы для MainPage"""
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators(object):
    """локаторы для LoginPage"""
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    """локаторы на странице добавления товара в корзину"""
    BUTTON_ADD_BASKET = (By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")
    MESSAGE_NAME_PRODUCT = (By.CSS_SELECTOR, "div.alertinner strong")
    NAME_PRODUCT = (By.CSS_SELECTOR, "div.col-sm-6.product_main h1")
    MESSAGE_PRICE_PRODUCT = (By.CSS_SELECTOR, "div.alertinner p strong")
    PRICE_PRODUCT = (By.CSS_SELECTOR, "div.col-sm-6.product_main p.price_color")