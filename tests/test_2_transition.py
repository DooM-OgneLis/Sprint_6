import allure
import pytest
from data import Urls, Const
from page.home_page import HomePage
from page.order_page import OrderPage


class TestTransitoins:
    @allure.title("проверка перехода с домашней страницы на страницу заказа")
    @allure.description("Главная → нажать на кнопку 'заказать'."
                        "произошел переход на форму заказа.")
    @pytest.mark.parametrize(
        "click_method_name",
        [
            ("click_on_order_button_head"),
            ("click_on_order_button_page"),
        ],
        ids=["head_button", "page_button"]
        )
    def test_click_on_order_button_head_transition_in_order_page(self, driver, click_method_name):
        home_page = HomePage(driver)
        home_page.url_start()
        
        click_method = getattr(home_page, click_method_name)
        click_method()
        
        assert home_page.is_url_opened(Urls.ORDER_PAGE_URL)

    @allure.title("проверка перехода со страницы заказа на главную страницы при нажатии на лого 'самокат'")
    @allure.description("страница заказа → нажать на лого 'самокат'."
                        "произошел переход на главную страницу самоката.")
    def test_click_on_scooter_logo_transition_in_home_page(self, driver):
        order_page = OrderPage(driver)
        order_page.set_start_url()
        
        order_page.click_on_scooter_logo()
        
        assert order_page.is_url_opened(Urls.HOME_PAGE_URL)

    @allure.title("проверка перехода на главную страницу дзен на главную страницу при нажатии на лого 'Яндекс'")
    @allure.description("страница заказа → нажать на лого 'Яндекс'."
                        "произошел переход на главную страницу дзен.")
    def test_click_on_yandex_logo_transition_in_dzen_page_home(self, driver):
        home_page = HomePage(driver)
        home_page.url_start()
        
        home_page.click_on_yandex_logo()

        home_page.switch_to_new_tab()
        
        assert home_page.is_url_opened(Urls.DZEN_HOME_URL+Const.REDIRRECT_KEY)
