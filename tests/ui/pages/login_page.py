from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.url = "https://automationexercise.com/login"
        self.email_input = (By.NAME, "email")
        self.password_input = (By.NAME, "password")
        self.login_button = (By.XPATH, "//button[@data-qa='login-button']")

    def open(self):
        self.driver.get(self.url)

    def login(self, email, password):
        self.wait.until(EC.visibility_of_element_located(self.email_input)).send_keys(email)
        self.driver.find_element(*self.password_input).send_keys(password)

        login_btn = self.wait.until(EC.presence_of_element_located(self.login_button))

        self.driver.execute_script("arguments[0].scrollIntoView(true);", login_btn)
        self.driver.execute_script("arguments[0].click();", login_btn)