

from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators


class ProductPage(BasePage):
    """Проверяем подстроку в адресной строке"""
    def should_be_promo_url(self):
        assert "?promo=newYear" in self.browser.current_url, "подстрока 'promo=newYear' отсутствует в url браузера"

    """Находим кнопку Добавить в корзину"""    
    def click_add_button(self):
        button_add_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_BASKET).click()

    """Считаем формулу в алерте"""    
    def calc_function(self):
        self.solve_quiz_and_get_code()

    """Проверяем имя товара в сообщении"""
    def message_name_product(self):
        #проверяем, что элемент Название товара есть в описании товара
        assert self.is_element_present(*ProductPageLocators.NAME_PRODUCT), (
            "Product name is not presented in description")
        #проверяем, что элемент Название товара есть в сообщении о добавлении товара в корзину
        assert self.is_element_present(*ProductPageLocators.MESSAGE_NAME_PRODUCT), (
            "Product name is not presented in message")

        #находим текст в элементе названия товара в описании и сообщении
        product_name = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        message_name = self.browser.find_element(*ProductPageLocators.MESSAGE_NAME_PRODUCT).text

        #делаем проверку, что текст совпадает
        assert product_name == message_name, "No product name in the message"
        

    """Проверяем цену товара в сообщении"""
    def message_price_product(self):
        assert self.is_element_present(*ProductPageLocators.NAME_PRODUCT), (
            "Product price is not presented in description")
        assert self.is_element_present(*ProductPageLocators.MESSAGE_NAME_PRODUCT), (
            "Product price is not presented in message")

        product_price = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        message_price = self.browser.find_element(*ProductPageLocators.MESSAGE_PRICE_PRODUCT).text

        assert product_price == message_price, "No product price in the message"

    """Функция проверки, что элемент НЕ появляется на странице в течении заданного времени"""    
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_NAME_PRODUCT), \
           "Success message is presented, but should not be"

    """Функция проверки, что элемент элемент исчезает на странице в течении заданного времени"""
    def should_be_success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_NAME_PRODUCT), \
           "Success message is not disappeared"





