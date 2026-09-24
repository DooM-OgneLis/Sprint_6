from data import Urls
import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.base_page_locators import BaseHeadingPageLocator as BPL

class BasePage:

    @allure.step("инициализация базового драйвера браузера и установка времени ожидания")
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открыть страницу в браузере: {url}")
    def url_start(self, url = Urls.HOME_PAGE_URL):
        self.driver.get(url)

    @allure.step("Ожидать, пока элемент станет видимым")
    def find_element_with_wait(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Кликнуть по элементу, дождавшись его кликабельности")
    def click_element_with_wait(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    @allure.step("Переключиться на новую вкладку")
    def switch_to_new_tab(self):
        all_tabs = self.driver.window_handles
        self.driver.switch_to.window(all_tabs[-1])

    @allure.step("Проверить, что URL {url} открыт")
    def is_url_opened(self, url):
        try:
            self.wait.until(EC.url_to_be(url))
            return True
        except TimeoutException:
            return False

    @allure.step("Дождаться видимости элемента {element}")
    def wait_element(self, element):
        self.wait.until(EC.visibility_of(element))
    
    @allure.step("Проскроллить к элементу {element} в центр экрана")
    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", element)

    @allure.step("Клик по кнопке заказа на чердаке страницы")
    def click_on_order_button_head(self):
        self.click_element_with_wait(BPL.BUTTON_ORDER_HEAD)

    @allure.step("Клик по логотипу Яндекса")
    def click_on_yandex_logo(self):
        self.click_element_with_wait(BPL.LOGO_YANDEX_HREF)

    @allure.step("Клик по логотипу Scooter")
    def click_on_scooter_logo(self):
        self.click_element_with_wait(BPL.LOGO_SCOOTER_HREF)   
