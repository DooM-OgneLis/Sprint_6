from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.base_page_locators import BaseHeadingPageLocator as BPL

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def url_start(self, URL):
        self.driver.get(URL)

    def find_element_with_wait(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click_element_with_wait(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def switch_to_new_tab(self):
        all_tabs = self.driver.window_handles
        self.driver.switch_to.window(all_tabs[-1])

    def is_url_opened(self, url):
        try:
            self.wait.until(EC.url_to_be(url))
            return True
        except TimeoutException:
            return False

    def wait_element(self, element):
        self.wait.until(EC.visibility_of(element))

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", element)

    def find_all_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click_on_order_button_head(self):
        self.click_element_with_wait(BPL.BUTTON_ORDER_HEAD)

    def click_on_yandex_logo(self):
        self.click_element_with_wait(BPL.LOGO_YANDEX_HREF)

    def click_on_Scooter_logo(self):
        self.click_element_with_wait(BPL.LOGO_SCOOTER_HREF)   