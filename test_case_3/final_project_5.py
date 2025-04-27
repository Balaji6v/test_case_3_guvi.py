import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
from pages3.login_pages import LoginPage
from pages3.inventory_page_5 import InventoryPage5

USERNAME = "standard_user"
PASSWORD = "secret_sauce"

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_random_product_selection(driver):
    login_page = LoginPage(driver)
    inventory_page_5 = InventoryPage5(driver)

    login_page.load()
    login_page.login(USERNAME,PASSWORD)

    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item")))

    products = inventory_page_5.get_all_products()
    assert len(products) == 6 , f"Expected 6 products,but found {len(products)}"

    selected = random.sample(products,4)
    for i, product in enumerate(selected,start=1):
        name = product.find_element(By.CLASS_NAME,"inventory_item_name").text
        price = product.find_element(By.CLASS_NAME,"inventory_item_price").text
        print(f"product {i} : {name} - {price}")
