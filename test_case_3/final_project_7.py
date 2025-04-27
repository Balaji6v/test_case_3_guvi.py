import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from pages3.login_pages import LoginPage
from pages3.inventory_page_7 import InventoryPage7
from pages3.cart_badge_7 import CartPage7

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()

def test_cart_verification(driver):
    login = LoginPage(driver)
    inventory_page_7 = InventoryPage7(driver)
    cart_badge = CartPage7(driver)

    login.load()
    login.login("standard_user","secret_sauce")

    inventory_page_7.add_first_product_to_cart()

    assert cart_badge.is_cart_badge_visible(), "cart is not visible"

    cart_badge.go_to_cart()

    items = cart_badge.get_cart_items()
    assert len(items) >= 1, "No products found in carts"

    for item in items:
        name = item.find_element(By.CLASS_NAME,"inventory_item_name").text
        price =  item.find_element(By.CLASS_NAME,"inventory_item_price").text
        print(f"product:{name},price:{price}")
        assert name.strip() != "", "Product nae is empty"
        assert price.strip() !="", "Product Price is empty"
