from selenium.webdriver.common.by import By 

class HomePageLocators:
    #локаторы блока о важном
    HEADER_QUESTION = (By.XPATH, "//div[text() = 'Вопросы о важном']")
    ACCORDION_BUTTONS = (By.XPATH, "//*[contains(@class, 'accordion__button')]")
    ACCORDION_PANELS = (By.XPATH, "//*[contains(@class, 'accordion__panel')]")

    #локаторы кнопок на заказ
    BUTTON_ORDER_PAGE = (By.XPATH, "//div[contains(@class, 'Home_FinishButton__1_cWm')]/button")