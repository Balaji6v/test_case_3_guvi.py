from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage8:
    def __init__(self,driver):
        self.driver = driver
        self.product_buttons = (By.CLASS_NAME,"btn_inventory")
        self.cart_icon = (By.CLASS_NAME,"shopping_cart_link")
        self.cart_badge = (By.CLASS_NAME,"shopping_cart_badge")

    def add_first_product_to_cart(self):
        buttons = WebDriverWait(self.driver,5).until(EC.presence_of_all_elements_located(self.product_buttons))
        self.driver.execute_script("arguments[0].click();",buttons[0])

    def get_cart_count(self):
        badge = WebDriverWait(self.driver,10).until(EC.presence_of_element_located(self.cart_badge))
        return int(badge.text)
    def go_to_cart(self):
        self.driver.find_element(*self.cart_icon).click()