from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckOutPage8:
    def __init__(self,driver):
        self.driver = driver
        self.checkout_btn = (By.ID,"checkout")
        self.first_name = (By.ID,"first-name")
        self.last_name = (By.ID,"last-name")
        self.postal_code = (By.ID,"postal-code")
        self.continue_btn = (By.ID,"continue")
        self.finish_btn = (By.ID,"finish")
        self.complete_header = (By.CLASS_NAME,"complete-header")
        self.cart_items = (By.CLASS_NAME,"cart_item")
        self.summary_info = (By.CLASS_NAME,"summary_info")

    def click_checkout(self):
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located(self.checkout_btn)).click()

    def fill_into_and_continue(self,first,last,postal):
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located(self.first_name)).send_keys(first)
        self.driver.find_element(*self.last_name).send_keys(last)
        self.driver.find_element(*self.postal_code).send_keys(postal)
        self.driver.find_element(*self.continue_btn).click()

    def validate_summary_page(self):
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located(self.summary_info))

    def validate_checkout_items(self):
        return self.driver.find_elements(*self.cart_items)

    def finish_order(self):
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.finish_btn)).click()

    def verify_confirmation(self):
        header = WebDriverWait(self.driver,10).until(EC.presence_of_element_located(self.complete_header))
        return "THANK YOU FOR YOUR ORDER" in header.text.upper()