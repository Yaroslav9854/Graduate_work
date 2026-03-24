from pages.page_main import MainPage
import allure
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import sleep

@pytest.mark.example_test
def test_check_test(driver_init):
    page = MainPage(driver_init)

    with allure.step("Открываем страницу браузера."):
        page.open_url("https://alfazdrav.ru/")

    with allure.step("Ждем текст заголовка на экране"):
        title_text = page.find_title_text()
        assert title_text

    with allure.step("Находим и наводимся на кнопку Врачи"):
        page.search_button_doctors(By.XPATH, '/html/body/div[1]/header/div/div[3]/div/div/div/nav/ul/li[2]/a')
        assert search_button_doctors



#     search_button = driver.find_element(By.XPATH, '/html/body/div[1]/header/div/div[3]/div/div/div/nav/ul/li[2]/a')
#     search_button.click()

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