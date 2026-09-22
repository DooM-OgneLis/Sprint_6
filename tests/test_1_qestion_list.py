import pytest
import allure
from data import Const
from page.home_page import HomePage



#проверка всех 8 вопросов на странице отдельными тестами
@pytest.mark.parametrize('element', range(Const.SCORE_IN_QUESTION))
class TestQestionList:

    @allure.title("Развертка ответа при выборе вопроса")
    @allure.description(
    "Главная → Вопросы о важном → нажать на вопрос. "
    "После блок с ответм развертывается под вопросом."
    )
    def test_click_in_qestion_makes_it_visible_answer(self, driver, element):
        home_page = HomePage(driver)

        home_page.url_start()

        home_page.click_on_quest_element(element)

        assert home_page.wait_open_element_answer(element)
