from page.base_page import BasePage
from data import Urls
from locators.order_page_locators import OrderFormLocators as OFL
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class OrderPage(BasePage):

    def url_start_set(self):
        self.url_start(Urls.ORDER_PAGE_URL)
    
    def write_one_page_in_form(self, first_name, second_name, address, metro, phone):
        self.find_element_with_wait(OFL.INPUT_FIRST_NAME).send_keys(first_name)
        self.find_element_with_wait(OFL.INPUT_LAST_NAME).send_keys(second_name)
        self.find_element_with_wait(OFL.INPUT_ADDRES).send_keys(address)
        self.find_element_with_wait(OFL.INPUT_METRO_STATION).send_keys(metro)

        option = self.wait.until(EC.element_to_be_clickable(OFL.LIST_METRO_STATION))
        option.click()

        self.find_element_with_wait(OFL.INPUT_PHONE_NUMBER).send_keys(phone)
        self.click_element_with_wait(OFL.BUTTON_NEXT_ORDER)

    def write_two_page_in_form(self, date_order, duration_text, color, comment):

        self.find_element_with_wait(OFL.INPUT_DATE_ORDER).send_keys(date_order)
        self.click_element_with_wait(OFL.NAME_PAGE_ORDER)
        self.click_element_with_wait(OFL.INPUT_LENGTH_ORDER)
        target_locator = (By.XPATH, f"//div[contains(@class, 'Dropdown-option') and normalize-space()='{duration_text}']")
        target_option = self.wait.until(EC.element_to_be_clickable(target_locator))
        target_option.click()
        if color[0]:
            self.click_element_with_wait(OFL.CHECKBOX_COLOR_BLACK)
        if color[1]:
            self.click_element_with_wait(OFL.CHECKBOX_COLOR_GREY)
        self.find_element_with_wait(OFL.INPUT_COMMENT).send_keys(comment)
        self.click_element_with_wait(OFL.BUTTON_ORDER)

        self.click_element_with_wait(OFL.BUTTON_ACCEPT_ORDER)

    def accept_order(self):
        self.find_element_with_wait(OFL.ORDER_MODAL)
        self.click_element_with_wait(OFL.BUTTON_ACCEPT_ORDER)
    
    def wait_next_pages_order(self):
        self.find_element_with_wait(OFL.NAME_PAGE_ORDER)