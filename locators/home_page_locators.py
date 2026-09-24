from selenium.webdriver.common.by import By 

class HomePageLocators:
    #локаторы кнопок на заказ
    BUTTON_ORDER_PAGE = (By.XPATH, "//div[contains(@class, 'Home_FinishButton__1_cWm')]/button")

    #макеты вызовов
    ACCORDION_HEADING = (By.ID, "accordion__heading-{}")
    ACCORDION_PANEL = (By.ID, "{}")