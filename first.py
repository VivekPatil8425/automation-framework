from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Step 1: Start the browser
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Step 2: Go to the practice site
driver.get("https://www.saucedemo.com/")

# Step 3: Find the username field and type into it
username_field = driver.find_element(By.ID, "user-name")
username_field.send_keys("standard_user")

# Step 4: Find the password field and type into it
password_field = driver.find_element(By.ID, "password")
password_field.send_keys("secret_sauce")

# Step 5: Find the login button and click it
login_button = driver.find_element(By.ID, "login-button")
login_button.click()

# Step 6: Pause so you can SEE it worked
time.sleep(5)

# Step 7: Close the browser
driver.quit()