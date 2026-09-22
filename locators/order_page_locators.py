from selenium.webdriver.common.by import By 

class OrderFormLocators:
    #поля заполнения
    #1 страница листа
    INPUT_FIRST_NAME = (By.XPATH, "//input[contains(@placeholder, '* Имя')]")
    INPUT_LAST_NAME = (By.XPATH, "//input[contains(@placeholder, '* Фамилия')]")
    INPUT_ADDRES = (By.XPATH, "//input[contains(@placeholder, '* Адрес: куда привезти заказ')]")
    INPUT_METRO_STATION = (By.XPATH, "//input[contains(@placeholder, '* Станция метро')]")
    INPUT_PHONE_NUMBER = (By.XPATH, "//input[contains(@placeholder, '* Телефон: на него позвонит курьер')]")
    #2 страница листа
    INPUT_DATE_ORDER = (By.XPATH, "//input[contains(@placeholder, '* Когда привезти самокат')]")
    INPUT_LENGTH_ORDER = (By.XPATH, "//div[contains(@class, 'Dropdown-control')]")
    CHECKBOX_COLOR_BLACK = (By.ID, "black")
    CHECKBOX_COLOR_GREY = (By.ID, "grey")
    INPUT_COMMENT = (By.XPATH, "//input[contains(@placeholder, 'Комментарий для курьера')]")

    #страница заказа
    NAME_PAGE_ORDER = (By.CLASS_NAME, "Order_Header__BZXOb")

    #список полей
    LIST_METRO_STATION = (By.XPATH, "//li[contains(@class, 'select-search__row')]/button")
    LIST_LENGTH_ORDER = (By.XPATH, "//div[contains(@class, 'Dropdown-option')]")

    #кнопки
    BUTTON_NEXT_ORDER = (By.XPATH, "//button[text() = 'Далее']") #переход на 2-ую страницу
    BUTTON_ORDER = (By.XPATH, "//div[contains(@class, 'Order_Buttons__1xGrp')]/button[text() = 'Заказать']") #оформить заказ
    BUTTON_ACCEPT_ORDER = (By.XPATH, "//div[contains(@class, 'Order_Buttons__1xGrp')]/button[text() = 'Да']") #подтвердить заказ
    BUTTON_CANCEL_ORDER = (By.XPATH, "//div[contains(@class, 'Order_Buttons__1xGrp')]/button[text() = 'Нет']") #подтвердить заказ

    #информационные блоки для подтверждения теста
    ORDER_MODAL = (By.CLASS_NAME, "Order_Modal__YZ-d3")
    ORDER_CREATED_INFORMATION = (By.XPATH, "//div[text() = 'Заказ оформлен']")

    #макеты вызовов
    DROPDOWN_OPTION_TEMPLATE = "//div[contains(@class, 'Dropdown-option') and normalize-space()='{}']"