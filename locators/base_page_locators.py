from selenium.webdriver.common.by import By 

class BaseHeadingPageLocator:
    #ссылки в логотипе
    LOGO_YANDEX_HREF = (By.XPATH, "//*[contains(@class, 'Header_LogoYandex__3TSOI')]")
    LOGO_SCOOTER_HREF = (By.XPATH, "//*[contains(@class, 'Header_LogoScooter__3lsAR')]")

    #кнопки в шапке
    BUTTON_ORDER = (By.XPATH, "//button[text() = 'Заказать']")