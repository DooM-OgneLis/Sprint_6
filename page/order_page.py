from page.base_page import BasePage
from data import Urls
import allure
from locators.order_page_locators import OrderFormLocators as OFL
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

class OrderPage(BasePage):

    @allure.step("Установить стартовый URL страницы заказа")
    def set_start_url(self):
        self.url_start(Urls.ORDER_PAGE_URL)

    @allure.step(
        "Заполнить первую страницу формы заказа: "
        "ФИО={first_name} {second_name}, адрес={address}, метро={metro}, телефон={phone}"
    )
    def write_one_page_in_form(self, first_name, second_name, address, metro, phone):
        self.find_element_with_wait(OFL.INPUT_FIRST_NAME).send_keys(first_name)
        self.find_element_with_wait(OFL.INPUT_LAST_NAME).send_keys(second_name)
        self.find_element_with_wait(OFL.INPUT_ADDRES).send_keys(address)
        self.find_element_with_wait(OFL.INPUT_METRO_STATION).send_keys(metro)

        self.click_element_with_wait(OFL.LIST_METRO_STATION)

        self.find_element_with_wait(OFL.INPUT_PHONE_NUMBER).send_keys(phone)
        self.click_element_with_wait(OFL.BUTTON_NEXT_ORDER)

    @allure.step(
        "Заполнить вторую страницу формы заказа: дата={date_order}, длительность={duration_text}, "
        "цвета(черный, серый)={color}, комментарий={comment}"
    )
    def write_two_page_in_form(self, date_order, duration_text, color, comment):

        self.find_element_with_wait(OFL.INPUT_DATE_ORDER).send_keys(date_order)
        self.click_element_with_wait(OFL.NAME_PAGE_ORDER)
        self.click_element_with_wait(OFL.INPUT_LENGTH_ORDER)
        target_locator = self.get_dropdown_option_locator(duration_text)
        self.click_element_with_wait(target_locator)
        if color[0]:
            self.click_element_with_wait(OFL.CHECKBOX_COLOR_BLACK)
        if color[1]:
            self.click_element_with_wait(OFL.CHECKBOX_COLOR_GREY)
        self.find_element_with_wait(OFL.INPUT_COMMENT).send_keys(comment)
        self.click_element_with_wait(OFL.BUTTON_ORDER)

    @allure.step("Подтвердить заказ в модальном окне")
    def accept_order(self):
        self.find_element_with_wait(OFL.ORDER_MODAL)
        self.click_element_with_wait(OFL.BUTTON_ACCEPT_ORDER)

    @allure.step("Дождаться появления заголовка следующей страницы заказа")
    def wait_next_pages_order(self):
        self.find_element_with_wait(OFL.NAME_PAGE_ORDER)


    def get_dropdown_option_locator(self, duration_text: str):
        xpath = OFL.DROPDOWN_OPTION_TEMPLATE.format(duration_text)
        return By.XPATH, xpath
    
    @allure.step("Проверить, открыто ли окно подтверждения создания заказа")
    def is_open_windows_order_complieted(self):
        try:
            self.find_element_with_wait(OFL.ORDER_CREATED_INFORMATION)
            return True
        except TimeoutException:
            return False
