from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import sleep
import allure

class BasePage:
    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 8)

    def open_url(self, url):
        self.driver.get(url)

    def wait_element(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element

    def click(self, locator):
        return self.wait_element(locator).click()

    def implicitly_wait(self):
        self.global_timeout = 10