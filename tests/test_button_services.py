from pages.page_main import MainPage
import allure
import pytest
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

    with allure.step("Находим и наводимся на кнопку Услуги"):
        page.select_services()

    with allure.step("Создаём 1 скриншот в качестве доказательства"):
        page.screenshot()

    with allure.step("Находим и наводимся на кнопку переключение отделений"):
        page.select_department()

    with allure.step("Создаём 2 скриншот в качестве доказательства"):
        page.screenshot()