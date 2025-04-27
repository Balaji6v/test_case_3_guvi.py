import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages3.login_pages import LoginPage
from pages3.inventory_page_8 import InventoryPage8
from pages3.checkout_page_8 import CheckOutPage8

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_checkout_flow_full(driver):
    login = LoginPage(driver)
    inventory_page_8 = InventoryPage8(driver)
    checkout_page_8 = CheckOutPage8(driver)

    login.load()
    login.login("standard_user", "secret_sauce")

    inventory_page_8.add_first_product_to_cart()
    assert inventory_page_8.get_cart_count() == 1

    inventory_page_8.go_to_cart()
    driver.save_screenshot("before_checkout_click.png")

    checkout_page_8.click_checkout()
    checkout_page_8.fill_into_and_continue("John", "Doe", "12345")

    checkout_page_8.validate_summary_page()
    driver.save_screenshot("checkout_overview.png")

    items = checkout_page_8.validate_checkout_items()
    assert len(items) == 1

    checkout_page_8.finish_order()
    assert checkout_page_8.verify_confirmation()
    print("Test case 8 passed: Full checkout flow successful.")