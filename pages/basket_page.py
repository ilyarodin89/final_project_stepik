
from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasketPageLocators

class BasketPage(BasePage):
    """функция проверяет, что товары в корзине не найдены"""
    def is_not_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Добавленные товары найдены в корзине"

    """функция проверяет, что присутствует текст Ваша корзина пуста"""
    def text_basket_empty_present(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_STATUS), (
            "Элемент с текстом, что корзина пуста, отсутствует")
