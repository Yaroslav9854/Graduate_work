import pytest
import allure
from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver import edge


@pytest.fixture(scope='function')
def driver_init():
    with allure.step("Создаем сессию драйвера"):
        driver_init = webdriver.Chrome()
        driver_init.maximize_window()
    yield driver_init
    driver_init.quit()


@pytest.fixture(scope='function')
def driver_new():
    with allure.step("Создаем сессию драйвера"):
        driver_new = webdriver.Edge()
        driver_new.maximize_window()
    yield driver_new
    driver_new.quit()


# @pytest.fixture(scope='function')
# def driver_init(request):
#     b = request.param
#     if b == 'edge':
#         browser = webdriver.Edge()
#     else:
#         browser = webdriver.Chrome()
#     browser.implicitly_wait(10)
#     yield browser
#     browser.quit()

# @pytest.fixture(scope="session")
# def config():
#     """Конфигурация тестов"""
#     return {
#         "base_url": "https://alfazdrav.ru/",
#         "timeout": 10,
#         "headless": True  # Установите False для визуального запуска
#     }