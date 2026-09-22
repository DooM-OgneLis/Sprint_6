import allure
from page.order_page import OrderPage
import pytest
from locators.order_page_locators import OrderFormLocators as OFL
@allure.title("проверка выполнения регистрации заказа")
@allure.description("страница заказа → заполнить поля пеервой страницы -> нажать 'далее' -> заполнить вторую страницу -> нажать на кнопку 'Заказать' -> подтвердить заказ нажатием 'Да'."
                    "Появилось информационное табло с номером заказа.")
class TestOrders:
    @pytest.mark.parametrize("run_id", list(range(2))) #выполнить тест 3 раза со случайными значениями
    def test_order_complited(self, driver, data_form, run_id):
        order_page = OrderPage(driver)
        order_page.url_start()

        order_page.click_on_order_button(run_id)

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
            'тестовый запуск'+str(run_id)
            )
        order_page.accept_order()

        assert order_page.is_open_windows_order_complieted()

