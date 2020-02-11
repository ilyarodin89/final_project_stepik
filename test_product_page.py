
import pytest
from selenium import webdriver
from pages.product_page import ProductPage
import time


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    link = (f"{link}")
    page = ProductPage(browser, link)
    page.open()
    #page.should_be_promo_url() #функция использовалась для проверки текста ?promo=newYear в адресной строке
    page.click_add_button() #нажимаем кнопку Добавить в корзину
    page.calc_function() #вычисляем функцию в alert, вписываем, скидываем alert
    page.message_name_product() #сравниваем название добавленного продукта в сообщении и описании
    page.message_price_product() #сравниваем цену добавленного продукта в сообщении и описании
    #time.sleep(15)
    






