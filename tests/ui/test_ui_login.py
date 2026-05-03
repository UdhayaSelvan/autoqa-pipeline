from tests.ui.pages.login_page import LoginPage
import allure

@allure.title("Invalid login with wrong credentials!")
def test_login_invalid(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("invalid@test.com", "wrongpassword")

    assert "login" in driver.current_url.lower()

@allure.title("The fields are empty!")
def test_login_empty_fields(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("", "")

    assert "login" in driver.current_url.lower()

@allure.title("Invalid email format!")
def test_login_invalid_email_format(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("invalid-email", "password")

    assert "login" in driver.current_url.lower()