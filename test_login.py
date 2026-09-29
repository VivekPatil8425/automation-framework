import csv
import os
# pytest is provided by the test runner; suppress editor diagnostics when the
# selected interpreter does not have the test dependencies installed.
# pyright: reportMissingImports=false
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage


def load_login_cases():
    base_dir = os.path.dirname(__file__)
    csv_path = os.path.join(base_dir, "test_data", "login_data.csv")
    cases = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            cases.append((row["username"], row["password"], row["expected_result"]))
    return cases


@pytest.mark.parametrize("username,password,expected", load_login_cases())
def test_login_scenarios(username, password, expected):
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(username, password)

    if expected == "success":
        assert "inventory" in driver.current_url, "Expected successful login"
    else:
        actual_error = login_page.get_error_message()
        assert expected in actual_error, f"Expected '{expected}', got '{actual_error}'"

    driver.quit()