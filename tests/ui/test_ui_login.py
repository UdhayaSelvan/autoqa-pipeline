import pytest
import csv
import allure
from tests.ui.pages.login_page import LoginPage


def load_test_data():
    with open("tests/data/login_data.csv", newline='') as file:
        reader = csv.DictReader(file)
        return [(row["email"], row["password"]) for row in reader]


@allure.title("Login test with multiple data inputs")
@pytest.mark.parametrize("email,password", load_test_data())
def test_login_data_driven(driver, email, password):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(email, password)

    assert "login" in driver.current_url.lower()