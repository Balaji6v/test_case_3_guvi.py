import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from pages3.login_pages import LoginPage

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--incognito")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service,options = options)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_logout_button(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user","secret_sauce")


    WebDriverWait(driver,10).until(EC.url_contains("inventory"))

    menu_btn = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"react-burger-menu-btn")))
    menu_btn.click()

    logout_btn = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"logout_sidebar_link")))
    assert logout_btn.is_displayed()
    logout_btn.click()

    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"login-button")))
    assert "saucedemo.com" in driver.current_url
