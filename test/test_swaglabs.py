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
    search_button = driver.find_element(By.XPATH, '//*[@id="menu-1-c2a71a6"]/li[2]/a')
    search_button.click()

    element = driver.find_element(By.XPATH, '//div[@class="elementor-button-wrapper"]')
    driver.execute_script("window.scrollBy(0, 900)")
    element.click()
    element.send_keys("Get In Touch")
    driver.get_screenshot_as_file("screenshot_About_us.png")