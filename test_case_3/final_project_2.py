from selenium import webdriver
from pages3.login_pages import LoginPage
import time


def test_login_invalid_user():
    driver = webdriver.Chrome()
    driver.maximize_window()

    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("guvi_user", "Secret@123")  # Invalid credentials

    time.sleep(2)  # optional, to wait for error message
    error_message = login_page.get_login_error_message()
    print("Captured error message:", error_message)

    assert "Username and password do not match" in error_message or "do not match" in error_message

    driver.quit()