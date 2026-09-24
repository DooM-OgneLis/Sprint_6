import allure
from page.home_page import HomePage
from page.order_page import OrderPage
import pytest

class TestOrders:

    @allure.title("проверка выполнения регистрации заказа")
    @allure.description("страница заказа → заполнить поля пеервой страницы -> нажать 'далее' -> заполнить вторую страницу -> нажать на кнопку 'Заказать' -> подтвердить заказ нажатием 'Да'."
                    "Появилось информационное табло с номером заказа.")
    @pytest.mark.parametrize(
    "click_method_name",
    [
        ("click_on_order_button_head"),
        ("click_on_order_button_page"),
    ],
    ids=["head_button", "page_button"]
    )
    def test_order_complited(self, driver, click_method_name, data_form):
        home_page = HomePage(driver)
        order_page = OrderPage(driver)
        order_page.url_start()

        click_method = getattr(home_page, click_method_name)
        click_method()

        order_page.write_one_page_in_form(
            data_form['first_name'],
            data_form['second_name'], 
            data_form['address'], 
            data_form['metro'], 
            data_form['phone']
            )
        order_page.wait_next_pages_order()
        order_page.write_two_page_in_form(
            data_form['date_order'], 
            data_form['length_order'], 
            data_form['color'], 
            'тестовый запуск'
            )
        order_page.accept_order()

        assert order_page.is_open_windows_order_complieted()

