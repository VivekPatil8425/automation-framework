from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    ZIP_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver):
        self.driver = driver

    def fill_info(self, first_name, last_name, zip_code):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.FIRST_NAME)).send_keys(first_name)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.LAST_NAME)).send_keys(last_name)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.ZIP_CODE)).send_keys(zip_code)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.CONTINUE_BUTTON)).click()
        WebDriverWait(self.driver, 10).until(EC.url_contains("checkout-step-two"))

    def finish_order(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.FINISH_BUTTON)).click()

    def get_success_message(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.SUCCESS_MESSAGE)).text