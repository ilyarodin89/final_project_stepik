
from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BUTTON_GO_TO_BASKET = (By.CSS_SELECTOR, "span.btn-group a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    """локаторы для MainPage"""
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    """локаторы для LoginPage"""
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTR_INPUT_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTR_INPUT_PASSWORD_1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTR_INPUT_PASSWORD_2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTR_SUBMIT_BUTTON = (By.NAME, "registration_submit")



class ProductPageLocators():
    """локаторы на странице товара"""
    BUTTON_ADD_BASKET = (By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")
    MESSAGE_NAME_PRODUCT = (By.CSS_SELECTOR, "div.alertinner strong")
    NAME_PRODUCT = (By.CSS_SELECTOR, "div.col-sm-6.product_main h1")
    MESSAGE_PRICE_PRODUCT = (By.CSS_SELECTOR, "div.alertinner p strong")
    PRICE_PRODUCT = (By.CSS_SELECTOR, "div.col-sm-6.product_main p.price_color")


class BasketPageLocators():
    """локаторы на странице Корзина"""
    BASKET_ITEMS = (By.CSS_SELECTOR, "div.basket-items")
    BASKET_STATUS = (By.CSS_SELECTOR, "#content_inner > p") #селектор, где выводится "Корзина пуста"