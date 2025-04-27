import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages3.login_pages import LoginPage
from pages3.inventory_page_4 import InventoryPage

USERNAME = "standard_user"
PASSWORD = "secret_sauce"

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()
def test_cart_button_visible(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    login_page.load()
    login_page.login(USERNAME,PASSWORD)

    assert inventory_page.is_cart_button_visible(), "cart is not visible"