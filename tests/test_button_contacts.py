from pages.page_main import MainPage
import allure
import pytest
import time

@pytest.mark.example_test
def test_check_test(driver_init):
    page = MainPage(driver_init)

    with allure.step("Открываем страницу браузера."):
        page.open_url("https://alfazdrav.ru/")

    with allure.step("Ждем текст заголовка на экране"):
        title_text = page.find_title_text()
        assert title_text

    with allure.step("Находим и наводимся на кнопку Контакты"):
        page.select_contacts()

    with allure.step("Ожидание: даем пользователю посмотреть на результат"):
        time.sleep(5)

    with allure.step("Ожидание: даем пользователю посмотреть на результат"):
        time.sleep(5)

    with allure.step("Находим и нажимаем на кнопку Клиника на Фрунзенской"):
        page.select_сlinic_frunzenskaya()

    with allure.step("Ожидание: даем пользователю посмотреть на результат"):
        time.sleep(5)

    with allure.step("Находим и нажимаем на кнопку Клиника на Спортивной"):
        page.select_clinic_sportivnaya()

    with allure.step("Ожидание: даем пользователю посмотреть на результат"):
        time.sleep(5)

    with allure.step("Находим и нажимаем на кнопку Клиника на Детская клиника на Спортивной"):
        page.select_clinic_sportivnaya_kids()

    with allure.step("Ожидание: даем пользователю посмотреть на результат"):
        time.sleep(5)

    with allure.step("Находим и нажимаем на кнопку Клиника на Новослободской"):
        page.select_clinic_novoslobodskaya()

    with allure.step("Ожидание: даем пользователю посмотреть на результат"):
        time.sleep(5)