import allure
from page.base_page import BasePage
from locators.home_page_locators import HomePageLocators as HPL
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

class HomePage(BasePage):
    @allure.step("Клик по кнопке заказа в теле страницы")
    def click_on_order_button_page(self):
        self.scroll_to_element(self.find_element_with_wait(HPL.BUTTON_ORDER_PAGE))
        self.click_element_with_wait(HPL.BUTTON_ORDER_PAGE)

    @allure.step("Возвращает локатор заголовка вопроса по индексу.")
    def get_heading_locator(self, index: int):
        by, template = HPL.ACCORDION_HEADING
        return by, template.format(index)

    @allure.step("Возвращает локатор панели ответа по индексу.")
    def get_panel_locator(self, index: int):
        by, template = HPL.ACCORDION_PANEL
        return by, template.format(index)

    @allure.step("Проверить, что аккордеон {index} открывается")
    def verify_accordion_opens(self, index: int) -> bool:
        heading_loc = self.get_heading_locator(index)
        panel_loc = self.get_panel_locator(index)

        # 1. Найти заголовок и проскроллить к нему
        heading = self.find_element_with_wait(heading_loc)
        self.scroll_to_element(heading)

        # 2. Дождаться кликабельности и кликнуть
        self.click_element_with_wait(heading_loc)

        # 3. Проверить aria-expanded у заголовка — самый надёжный способ
        if heading.get_attribute("aria-expanded") == "true":
            return True

        # 4. Запасной вариант: проверить, что у панели нет атрибута hidden
        panel = self.find_element_with_wait(panel_loc)
        return panel.get_attribute("hidden") is None