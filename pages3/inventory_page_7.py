from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage7:
    def __init__(self,driver):
        self.driver = driver
        self.add_button = (By.CLASS_NAME,"btn_inventory")

    def add_first_product_to_cart(self):
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.add_button)).click()