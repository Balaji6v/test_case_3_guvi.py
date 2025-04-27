from selenium.webdriver.common.by import By
from selenium import webdriver
import random


class InventoryPage5:
    def __init__(self,driver):
        self.driver = driver
        self.product_list = (By.CLASS_NAME,"inventory_item")

    def get_all_products(self):
        return self.driver.find_elements(*self.product_list)
    def get_random_products(self,count=4):
        all_products = self.get_all_products()
        return random.sample(all_products,count)