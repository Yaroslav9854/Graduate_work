import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome ()

driver.get("https://swaglabs.in/")
driver.maximize_window()
driver.implicitly_wait(10)

@pytest.fixture(scope='function')
def close_session():
    yield
    driver.quit()

def test_click(close_session):
    search = driver.find_element(By.CSS_SELECTOR, "")
    search.click()

    search_button = driver.find_element(By.CSS_SELECTOR, "")
    search_button.click()