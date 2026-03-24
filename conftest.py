import pytest
import allure
from selenium import webdriver

@pytest.fixture(scope='function')
def driver_init():
    with allure.step("Создаем сессию драйвера"):
        driver_init = webdriver.Chrome()
    yield driver_init
    driver_init.quit()

# @pytest.fixture(scope='function')
# def driver_init():
#
# @pytest.fixture(scope="session")
# def config():
#     """Конфигурация тестов"""
#     return {
#         "base_url": "https://alfazdrav.ru/",
#         "timeout": 10,
#         "headless": True  # Установите False для визуального запуска
#     }