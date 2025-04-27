import pytest
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from pages3.login_pages import LoginPage
from pages3.inventory_page_6 import InventoryPage6

USERNAME = "standard_user"
PASSWORD = "secret_sauce"


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()

def test_random_product_selection(driver):
    login_page = LoginPage(driver)
    inventory_page_6 = InventoryPage6(driver)

    login_page.load()
    login_page.login(USERNAME,PASSWORD)

    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,"inventory_item")))

    buttons = inventory_page_6.get_add_cart_buttons()
    assert len(buttons) >=6, f"Expected at least 6 products, found {len(buttons)}"

    selected = random.sample(buttons,4)



    for btn in selected:
        driver.execute_script("arguments[0].click();",btn)


    count = inventory_page_6.get_cart_count()
    assert count == 4,f"Expected  4 items in cart, but found {count}"