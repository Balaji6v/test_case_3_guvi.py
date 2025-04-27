from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class InventoryPage:
    def __init__(self,driver):
        self.driver = driver
        self.wait =  WebDriverWait(driver,10)

    def is_cart_button_visible(self):
        cart_btn = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"shopping_cart_link")))
        return cart_btn.is_displayed()