import allure
from data import Urls, Const
from page.home_page import HomePage
from page.order_page import OrderPage

@allure.title("проверка перехода с домашней страницы на страницу заказа")
@allure.description("Главная → нажать на кнопку 'заказать' в чердаке страницы."
                    "произошел переход на форму заказа.")
def test_click_on_order_button_head_transition_in_order_page(driver):
    home_page = HomePage(driver)
    home_page.url_start_set()
    
    home_page.click_on_order_button_head()
    
    assert home_page.is_url_opened(Urls.ORDER_PAGE_URL)

@allure.title("проверка перехода с домашней страницы на страницу заказа")
@allure.description("Главная → нажать на кнопку 'заказать' в теле страницы."
                    "произошел переход на форму заказа.")
def test_click_on_order_button_page_transition_in_order_page(driver):
    home_page = HomePage(driver)
    home_page.url_start_set()
    
    home_page.click_on_order_button_page()
    
    assert home_page.is_url_opened(Urls.ORDER_PAGE_URL)

@allure.title("проверка перехода со страницы заказа на главную страницы при нажатии на лого 'самокат'")
@allure.description("страница заказа → нажать на лого 'самокат'."
                    "произошел переход на главную страницу самоката.")
def test_click_on_Scooter_logo_transition_in_home_page(driver):
    order_page = OrderPage(driver)
    order_page.url_start_set()
    
    order_page.click_on_Scooter_logo()
    
    assert order_page.is_url_opened(Urls.HOME_PAGE_URL)

@allure.title("проверка перехода на главную страницу дзен на главную страницу при нажатии на лого 'Яндекс'")
@allure.description("страница заказа → нажать на лого 'Яндекс'."
                    "произошел переход на главную страницу дзен.")
def test_click_on_yandex_logo_transition_in_dzen_page_home(driver):
    home_page = HomePage(driver)
    home_page.url_start_set()
    
    home_page.click_on_yandex_logo()

    home_page.switch_to_new_tab()
    
    assert home_page.is_url_opened(Urls.DZEN_HOME_URL+Const.REDIRRECT_KEY)
