from pages.page_main import MainPage
import allure
import pytest
from selenium.webdriver.support.expected_conditions import element_to_be_selected
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import sleep
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService



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