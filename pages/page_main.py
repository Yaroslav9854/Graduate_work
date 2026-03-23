from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.expected_conditions import title_is
import time


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    TITLE_TEXT = (By.XPATH, "//h1[text() = 'Example Domain']")


    def find_title_text(self):
        return self.wait_element(self.TITLE_TEXT)

    def check_tabs(self):
        tabs = self.wait_elements(self.MAIN.TABS)
        for tab in tabs:
            self.driver.execute_script("", tabs)
            tab.click()
            text = tab.text
            tab.click()
            title = self.driver.find_element(By.XPATH, f"")
            assert text == title.text
            time.sleep(3)

    def select_promotions(self):
        self.click(self.PROMOTIONS)

    def select_dodocoins(self):
        self.click(self.DODOCOINS)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)
        time.sleep(3)

    def click_button(self):
        self.click(self.Doctors)
        time.sleep(3)

    def click_tabs(self):
        tabs = self.wait_elements(self.BUTTON.TABS)
        for tab in tabs:
            self.driver.execute_script("", tabs)
            tab.click()

    def open_url(self):
     search_button = driver.find_element(By.XPATH, '/html/body/div[1]/header/div/div[3]/div/div/div/nav/ul/li[2]/a')
     search_button.click()