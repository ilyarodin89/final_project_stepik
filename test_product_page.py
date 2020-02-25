
import pytest
from pages.product_page import ProductPage
from pages.login_page import LoginPage

"""
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


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.click_add_button() #нажимаем кнопку Добавить в корзину
    page.should_not_be_success_message() #проверяем, что нет соообщения об успехе


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message() #проверяем, что нет соообщения об успехе


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.click_add_button() #нажимаем кнопку Добавить в корзину
    page.should_be_success_message_is_disappeared() #проверяем, что сообщение о добавлении в корзину исчезает в течении
    # установленного времени


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.is_not_product_in_basket()
    basket_page.text_basket_empty_present()
    
"""


"""тесты из раздела 4.3 урок 13 (тесты для залогиненного пользователя)"""
@pytest.mark.auth_user
class TestUserAddToBasketFromProductPage(object):
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user()
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()  # проверяем, что нет соообщения об успехе

    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.click_add_button()  # нажимаем кнопку Добавить в корзину
        #page.solve_quiz_and_get_code()  # вычисляем функцию в alert, вписываем, скидываем alert
        #ЗАКОММЕНТИРОВАЛ ЭТУ ФУНКЦИЮ, Т.К. АЛЕРТА НЕТ И ТЕСТ ПАДАЛ ИЗ-ЗА ЕГО ОТСУТСТВИЯ
        page.message_name_product()  # сравниваем название добавленного продукта в сообщении и описании
        page.message_price_product()  # сравниваем цену добавленного продукта в сообщении и описании



