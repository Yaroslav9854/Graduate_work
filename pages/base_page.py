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

    # def scroll_to_element(self, locator, attempts=5):
    #     self.global_timeout = 2
    #     element = None
    #     counter = 0
    #     while counter < attempts:
    #         self.driver.execute_script("window.scrollBy(0, 900);")
    #         sleep(1)
    #         try:
    #             element = self.wait.until(EC.visibility_of_element_located(locator))
    #             return element
    #         except TimeoutException:
    #             counter += 1
    #             continue
    #     return element

    #
    # def wait_element(self, locator):
    #     return self.wait.until(EC.visibility_of_element_located(locator))
    #
    # def wait_elements(self, locator):
    #     return self.wait.until(EC.visibility_of_all_elements_located(locator))
    #
    # def click(self, locator):
    #     return self.wait_element(locator).click()
    #
    # def take_screenshot(self, text):
    #     allure.attach(
    #         self.driver.get_screenshot_as_png(),
    #         name-text,
    #         attachment_type=allure.attachment_type.PNG
    #     )