Нужно написать фикстуру в которой будет создаваться сессия драйвера и закрываться после прохождения.
Нужно написать конструктор в Main_Page который примет объект драйвера и передаст его в класс родитель BasePage.
driver = webdriver.Chrome ()

driver.get("https://alfazdrav.ru/")
driver.maximize_window()
driver.implicitly_wait(10)

@pytest.fixture(scope='function')
def close_session():
    yield
    driver.quit()