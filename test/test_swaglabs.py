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

def scroll_to_element(self, locator, attempts=5):
    self.global_timeout = 2
    element = None
    counter = 0
    while counter < attempts:
        self.driver.execute_script("window.scrollBy(0, 900);")
        sleep(1)
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            return element
        except TimeoutException:
            counter += 1
            continue
    return element