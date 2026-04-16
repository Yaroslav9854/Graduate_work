from pages.page_main import MainPage
import allure
import pytest
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import sleep

@pytest.mark.example_test
def test_check_test(driver_init):
    page = MainPage(driver_init)

    with allure.step("Открываем страницу браузера."):
        page.open_url("https://alfazdrav.ru/")

    with allure.step("Ждем текст заголовка на экране"):
        title_text = page.find_title_text()
        assert title_text

    with allure.step("Находим и наводимся на стрелку вправо"):
        page.select_right()

    with allure.step("Ожидание: даем пользователю посмотреть на результат"):
        time.sleep(5)

    with allure.step("Находим и наводимся на стрелку вправо"):
        page.select_right()

    with allure.step("Ожидание: даем пользователю посмотреть на результат"):
        time.sleep(5)

    with allure.step("Находим и наводимся на стрелку влево"):
        page.select_left()

    with allure.step("Ожидание: даем пользователю посмотреть на результат"):
        time.sleep(5)

    with allure.step("Находим и наводимся на стрелку влево"):
        page.select_left()

    with allure.step("Ожидание: даем пользователю посмотреть на результат"):
        time.sleep(5)