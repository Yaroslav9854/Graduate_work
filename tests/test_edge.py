from pages.page_main import MainPage
import allure
import pytest
import time

@pytest.mark.example_test
def test_check_edge(driver_new):
    page = MainPage(driver_new)

    with allure.step("Открываем страницу браузера."):
        page.open_url("https://alfazdrav.ru/")

    with allure.step("Ждем текст заголовка на экране"):
        title_text = page.find_title_text()
        assert title_text

    with allure.step("Находим и наводимся на кнопку Цены"):
        page.select_prices()

    with allure.step("Ожидание: даем пользователю посмотреть на результат"):
        time.sleep(5)