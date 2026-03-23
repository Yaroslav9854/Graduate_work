import pytest
from selenium import webdriver
import allure

@pytest.fixture(scope='function')
def driver_init():
    with allure.step("Создаем сессию драйвера"):
        driver_init = webdriver.Chrome()
    yield driver_init
    driver_init.quit()