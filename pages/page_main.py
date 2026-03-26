from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.expected_conditions import title_is
import time


class MainPage(BasePage):
    TITLE_TEXT = (By.XPATH, "/html/body/div[1]/header/div/div[1]/div[2]/div/div/div/div[1]/img")
    DOCTORS = (By.XPATH, "/html/body/div/header/div/div[3]/div/div/div/nav/ul/li[2]/a")
    CONTACTS = (By.XPATH, "/html/body/div[1]/header/div/div[3]/div/div/div/nav/ul/li[10]/a")
    PRICES = (By.XPATH, "/html/body/div[1]/header/div/div[3]/div/div/div/nav/ul/li[6]/a")
    REVIEWS = (By.XPATH, "/html/body/div[1]/header/div/div[3]/div/div/div/nav/ul/li[9]/a")
    SCHEDULE = (By.XPATH, "/html/body/div[1]/header/div/div[3]/div/div/div/nav/ul/li[5]/span")
    SERVICES = (By.XPATH, "/html/body/div[1]/header/div/div[3]/div/div/div/nav/ul/li[3]/a")
    STOCKS = (By.XPATH, "/html/body/div[1]/header/div/div[3]/div/div/div/nav/ul/li[7]/a")


    def __init__(self, driver):
        super().__init__(driver)

    def find_title_text(self):
        return self.wait_element(self.TITLE_TEXT)

    def select_doctors(self):
        self.click(self.DOCTORS)

    def select_contacts(self):
        self.click(self.CONTACTS)

    def select_prices(self):
        self.click(self.PRICES)

    def select_reviews(self):
        self.click(self.REVIEWS)

    def select_schedule(self):
        self.click(self.SCHEDULE)

    def select_services(self):
        self.click(self.SERVICES)

    def select_stocks(self):
        self.click(self.STOCKS)


    # def check_tabs(self):
    #     tabs = self.wait_elements(self.MAIN.TABS)
    #     for tab in tabs:
    #         self.driver.execute_script("", tabs)
    #         tab.click()
    #         text = tab.text
    #         tab.click()
    #         title = self.driver.find_element(By.XPATH, f"/html/body/div[1]/header/div/div[1]/div[2]/div/div/div/div[1]/img[text()='{АЛЬФА ЦЕНТР ЗДОРОВЬЯ}']")
    #         assert text == title.text
    #         time.sleep(3)

    # def open_url(self):
    #  search_button = find_element(By.XPATH, '/html/body/div[1]/header/div/div[3]/div/div/div/nav/ul/li[2]/a')
    #  search_button.click()
    #
    #
    # def select_promotions(self):
    #     self.click(self.PROMOTIONS)
    #
    # def select_dodocoins(self):
    #     self.click(self.DODOCOINS)
    #
    # def click_login(self):
    #     self.click(self.LOGIN_BUTTON)
    #     time.sleep(3)
    #
    # def click_button(self):
    #     self.click(self.Doctors)
    #     time.sleep(3)
    #
    # def click_tabs(self):
    #     tabs = self.wait_elements(self.BUTTON.TABS)
    #     for tab in tabs:
    #         self.driver.execute_script("", tabs)
    #         tab.click()