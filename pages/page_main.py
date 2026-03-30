from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.support import expected_conditions as EC
import time
from time import sleep
from selenium.common.exceptions import TimeoutException


class MainPage(BasePage):
    TITLE_TEXT = (By.XPATH, "/html/body/div[1]/header/div/div[1]/div[2]/div/div/div/div[1]/img")
    DOCTORS = (By.XPATH, "/html/body/div/header/div/div[3]/div/div/div/nav/ul/li[2]/a")
    CONTACTS = (By.XPATH, "/html/body/div[1]/header/div/div[3]/div/div/div/nav/ul/li[10]/a")
    PRICES = (By.XPATH, "/html/body/div[1]/header/div/div[3]/div/div/div/nav/ul/li[6]/a")
    REVIEWS = (By.XPATH, "/html/body/div[1]/header/div/div[3]/div/div/div/nav/ul/li[9]/a")
    SCHEDULE = (By.XPATH, "/html/body/div[1]/header/div/div[3]/div/div/div/nav/ul/li[5]/span")
    SERVICES = (By.XPATH, "/html/body/div[1]/header/div/div[3]/div/div/div/nav/ul/li[3]/a")
    STOCKS = (By.XPATH, "/html/body/div[1]/header/div/div[3]/div/div/div/nav/ul/li[7]/a")
    HELP_DOCTOR = (By.XPATH, "/html/body/div[1]/main/div[2]/div/div/div/div/div[5]/div/div[18]/div/div[1]/a[2]")
    DEPARTMENT = (By.XPATH, "/html/body/div[1]/main/div[2]/div/div/div/div[2]/div/div[1]/div/label/span")
    FRUNZENSKAYA = (By.XPATH, "//a[@data-id='38727']")
    SPORTIVNAYA = (By.XPATH, "//a[@data-id='776317']")
    SPORTIVNAYA_KIDS = (By.XPATH, "")
    NOVOSLOBODSKAYA = (By.XPATH, "")
    NOVOKUZNETSK = (By.XPATH, "")
    BAUMANSKAYA = (By.XPATH, "")


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

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

    def select_help_doctor(self):
        self.click(self.HELP_DOCTOR)

    def select_сlinic_frunzenskaya(self):
        self.click(self.FRUNZENSKAYA)

    def select_clinic_sportivnaya(self):
        self.click(self.SPORTIVNAYA)

    def select_clinic_sportivnaya_kids(self):
        self.click(self.SPORTIVNAYA_KIDS)

    def select_clinic_novoslobodskaya(self):
        self.click(self.NOVOSLOBODSKAYA)

    def select_clinic_novokuznetsk(self):
        self.click(self.NOVOKUZNETSK)

    def select_clinic_baumanskaya(self):
        self.click(self.BAUMANSKAYA)

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

    def screenshot(self, name: str = "screenshot.png"):
        self.driver.get_screenshot_as_file(name)
        # self.driver.get_screenshot_as_file("screenshot2.png")

    def select_department(self):
        self.click(self.DEPARTMENT)

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
