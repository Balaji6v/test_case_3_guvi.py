
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from pages3.login_pages import LoginPage
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()



@pytest.mark.parametrize("username", [
    "standard_user",
    "problem_user",
    "performance_glitch_user",
    "locked_out_user"
])

def test_login_multiple_users(driver, username):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login(username, "secret_sauce")

    if username == "locked_out_user":
        error_msg = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "error-message-container")))
        assert error_msg.is_displayed()
    else:
        assert "inventory" in driver.current_url