from data import Urls
from page.base_page import BasePage
from locators.home_page_locators import HomePageLocators as HPL

class HomePage(BasePage):

    def url_start_set(self):
        self.url_start(Urls.HOME_PAGE_URL)

    def click_on_order_button_page(self):
        self.scroll_to_element(self.find_element_with_wait(HPL.BUTTON_ORDER_PAGE))
        self.click_element_with_wait(HPL.BUTTON_ORDER_PAGE)

    def click_on_quest_element(self, element = 0):
        question = self.find_all_elements(HPL.ACCORDION_BUTTONS) 
        self.scroll_to_element(question[element]) #перемещаемся к элементу для клика, в противном случае кликает в пустоту
        self.click_element_with_wait(question[element])

    def wait_open_element_answer(self, element = 0):
        answer = self.find_all_elements(HPL.ACCORDION_PANELS)
        self.wait_element(answer[element])
        return answer[element].is_displayed()
