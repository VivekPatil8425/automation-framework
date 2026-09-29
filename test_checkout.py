from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_complete_checkout_flow():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    inventory_page.add_product_to_cart("sauce-labs-backpack")
    assert inventory_page.get_cart_count() == "1", "Cart badge should show 1 item"

    inventory_page.go_to_cart()
    cart_page = CartPage(driver)
    cart_page.checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.fill_info("Vivek", "Patil", "411001")
    checkout_page.finish_order()

    success_message = checkout_page.get_success_message()
    assert "Thank you" in success_message, f"Expected order confirmation, got '{success_message}'"

    driver.quit()