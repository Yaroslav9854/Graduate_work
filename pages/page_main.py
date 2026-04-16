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
    HELP_DOCTOR = (By.XPATH, "//a[text()='Туранкова Таисия Алексеевна']")
    DEPARTMENT = (By.XPATH, "/html/body/div[1]/main/div[2]/div/div/div/div[2]/div/div[1]/div/label/span")
    FRUNZENSKAYA = (By.XPATH, "//a[@data-id='38727']")
    SPORTIVNAYA = (By.XPATH, "//a[@data-id='776317']")
    SPORTIVNAYA_KIDS = (By.XPATH, "//a[@data-id='776323']")
    NOVOSLOBODSKAYA = (By.XPATH, "//a[@data-id='776330']")
    FIND_CONTACTS = (By.XPATH, "//a[b-contacts-page__title='Клиники «Альфа-Центр Здоровья» в Москве'")
    FIND_FRUNZENSKAYA = (By.XPATH, "/html/body/div/main/div[2]/div/div/div/h1")
    FIND_SPORTIVNAYA_KIDS = (By.XPATH, "/html/body/div/main/div[2]/div/div/div/h1")
    FIND_NOVOSLOBODSKAYA = (By.XPATH, "/html/body/div/main/div[2]/div/div/div/h1")
    FIND_NOVOKUZNETSK = (By.XPATH, "/html/body/div/main/div[2]/div/div/div/h1")
    FIND_BAUMANSKAYA = (By.XPATH, "/html/body/div/main/div[2]/div/div/div/h1")
    fond = (By.XPATH, "")
    ADDRESS_GRAPHIC = (By.XPATH, "/html/body/div[1]/header/div/div[1]/div[1]/div/div/div/div[4]/div[2]/div[1]")
    RIGHT = (By.XPATH, "/html/body/div[1]/main/div[1]/div/div[2]/div[2]/div/div/div/div/div[2]/div[2]/div/div/div[3]")
    LEFT = (By.XPATH, "/html/body/div[1]/main/div[1]/div/div[2]/div[2]/div/div/div/div/div[2]/div[2]/div/div/div[1]/img")
    TECHNIQUES = "//*[@id='price-page']/div/div[3]/div/div[2]/div[1]/div"

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

    def select_city_selection(self):
        self.click(self.fond)

    def select_city_perm(self):
        self.click(self.fond)

    def select_feedback(self):
        self.click(self.fond)

    def select_address(self):
        self.click(self.ADDRESS_GRAPHIC)

    def select_record(self):
        self.click(self.fond)

    def select_right(self):
        self.click(self.RIGHT)

    def select_left(self):
        self.click(self.LEFT)

    def select_techniques(self):
        self.click(self.TECHNIQUES)

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
