from pages.login_page import LoginPage

def test_authorization(driver):
    auth = LoginPage(driver)
    auth.input_email()
    auth.input_password()
    auth.click_auth_btn()