from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver

    def add_product_to_cart(self, product_slug):
        # product_slug example: "sauce-labs-backpack"
        locator = (By.ID, f"add-to-cart-{product_slug}")
        button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].click();", button)

    def get_cart_count(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.CART_BADGE)).text

    def go_to_cart(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.CART_LINK)).click()
        WebDriverWait(self.driver, 10).until(EC.url_contains("cart.html"))