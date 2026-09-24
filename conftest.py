import pytest
import generator
from data import Const, Urls
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Firefox()
    driver.get(Urls.HOME_PAGE_URL)
    yield driver
    driver.quit()

@pytest.fixture(scope="function") #для проверки формы подходит, каждый раз новые данные
def data_form():
    address = generator.random_in_list(Const.ADDRESS)  # сначала сохраняем выбранный адрес
    address_index = Const.ADDRESS.index(address)       # потом находим его индекс
    metro = Const.METRO[address_index]
    return {
        "first_name": generator.random_in_list(Const.FIRST_NAME),
        "second_name": generator.random_in_list(Const.LAST_NAME),
        "address": address,
        "metro": metro,
        "phone": generator.random_phone(),
        "date_order": generator.random_date_for_delivery(),
        "length_order": generator.random_in_list(Const.DURATION_OPTIONS),
        "color": [generator.random_boolian(), generator.random_boolian()]
    }