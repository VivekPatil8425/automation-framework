# automation-framework

**Status: In Progress**

## Overview

A Python UI automation project for [SauceDemo](https://www.saucedemo.com/), built with Selenium and pytest. The tests use page objects to keep browser interactions organized.

## Current Coverage

- Login scenarios for valid credentials, a locked-out user, and an incorrect password, with cases loaded from a CSV file.
- An end-to-end checkout test that signs in, adds a product to the cart, enters checkout information, and verifies the order confirmation.
- `first.py`, a standalone browser script demonstrating a successful login.

## Project Structure

```text
automation_framework/
|-- first.py
|-- test_login.py
|-- test_checkout.py
|-- pages/
|   |-- login_page.py
|   |-- inventory_page.py
|   |-- cart_page.py
|   `-- checkout_page.py
`-- test_data/
|   `-- login_data.csv
```

The browser tests use Chrome and `webdriver-manager` to obtain ChromeDriver.
