from selenium.webdriver.common.by import By 

class BaseHeadingPageLocator:
    #ссылки в логотипе
    LOGO_YANDEX_HREF = (By.XPATH, "//*[contains(@class, 'Header_LogoYandex__3TSOI')]")
    LOGO_SCOOTER_HREF = (By.XPATH, "//*[contains(@class, 'Header_LogoScooter__3lsAR')]")

    #кнопки в шапке
    BUTTON_ORDER_HEAD = (By.XPATH, "//div[contains(@class, Header_Header__214zg)]/*/button[text() = 'Заказать']")