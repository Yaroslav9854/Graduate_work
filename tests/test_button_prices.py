from pages.page_main import MainPage
import allure
import pytest
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

@pytest.mark.example_test
def test_check_test(driver_init):
    page = MainPage(driver_init)

    with allure.step("Открываем страницу браузера."):
        page.open_url("https://alfazdrav.ru/")

    with allure.step("Ждем текст заголовка на экране"):
        title_text = page.find_title_text()
        assert title_text

    with allure.step("Находим и наводимся на кнопку Цены"):
        page.select_prices()

    with allure.step("Ожидание: даем пользователю посмотреть на результат"):
        time.sleep(5)

    with allure.step("Создаём скриншот в качестве доказательства"):
        page.screenshot("screen_prices.png")