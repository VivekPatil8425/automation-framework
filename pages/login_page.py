from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username, password):
        self.driver.find_element(*self.USERNAME_INPUT).clear()
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT).clear()
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()

        try:
            WebDriverWait(self.driver, 10).until(EC.url_contains("inventory"))
        except Exception:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.ERROR_MESSAGE))

    def get_error_message(self):
        return self.driver.find_element(*self.ERROR_MESSAGE).text