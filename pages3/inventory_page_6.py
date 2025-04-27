from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage6:
    def __init__(self,driver):
        self.driver = driver
        self.product_selector = (By.CLASS_NAME,"inventory_item")
        self.product_name = (By.CLASS_NAME,"inventory_item_name")
        self.product_price = (By.CLASS_NAME,"inventory_item_price")
        self.add_to_cart_buttons = (By.XPATH,"//button[contains(text(),'Add to cart')]")
        self.cart_badge = (By.CLASS_NAME,"shopping_cart_badge")

    def get_all_products(self):
        return self.driver.find_elements(*self.product_selector)

    def get_add_cart_buttons(self):
        return self.driver.find_elements(*self.add_to_cart_buttons)

    def get_cart_count(self):
        try:
            badge = WebDriverWait(self.driver,5).until(EC.presence_of_element_located(self.cart_badge))
            return int (badge.text)
        except:
            return 0