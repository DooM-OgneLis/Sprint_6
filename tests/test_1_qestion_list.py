import pytest
import allure
from page.home_page import HomePage



#проверка всех 8 вопросов на странице отдельными тестами
class TestQestionList:
    # Словарь: индекс → понятное описание
    QUESTION_DESCRIPTIONS = {
        0: "price_and_payment",
        1: "multiple_scooters",
        2: "rent_time_calculation",
        3: "order_today",
        4: "extend_or_return_early",
        5: "charger_delivery",
        6: "cancel_order",
        7: "outside_mkad"
    }

    @allure.title("Развертка ответа: {question_desc}")
    @allure.description(
        "Главная → Вопросы о важном → нажать на вопрос «{question_desc}». "
        "После блок с ответом разворачивается под вопросом."
    )
    @pytest.mark.parametrize(
        "question_number",
        [0, 1, 2, 3, 4, 5, 6, 7],
        ids=list(QUESTION_DESCRIPTIONS.values())  # это для pytest-вывода в консоль
    )
    def test_accordion_opens_correct_panel(self, driver, question_number):
        question_desc = self.QUESTION_DESCRIPTIONS[question_number]

        allure.dynamic.title(f"[Q{question_number}] Развертка: {question_desc}")
        allure.dynamic.description(
            f"Индекс: {question_number} | Вопрос: «{question_desc}»\n"
            "Действие: клик по заголовку аккордеона.\n"
            "Ожидаемый результат: панель ответа становится видимой."
        )
        home_page = HomePage(driver)

        assert home_page.verify_accordion_opens(question_number) is True
