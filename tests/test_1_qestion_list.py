import pytest
import allure
from data import Const
from page.home_page import HomePage

@allure.title("Развертка ответа при выборе вопроса")
@allure.description("Главная → Вопросы о важном → нажать на вопрос."
                    "После блок с ответм развертывается под вопросом.")

#проверка всех 8 вопросов на странице отдельными тестами
@pytest.mark.parametrize('element', range(Const.SCORE_IN_QUESTION))
def test_click_in_qestion_makes_it_visible_answer(driver, element):
    home_page = HomePage(driver)
    home_page.url_start_set()

    home_page.click_on_quest_element(element)

    assert home_page.wait_open_element_answer(element)
