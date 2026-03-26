import pytest
import allure
from selenium import webdriver
from selenium.webdriver import chrome


@pytest.fixture(scope='function')
def driver_init():
    with allure.step("Создаем сессию драйвера"):
        driver_init = webdriver.Chrome()
        driver_init.maximize_window()
    yield driver_init
    driver_init.quit()

# @pytest.fixture(scope="session")
# def config():
#     """Конфигурация тестов"""
#     return {
#         "base_url": "https://alfazdrav.ru/",
#         "timeout": 10,
#         "headless": True  # Установите False для визуального запуска
#     }