import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


from HW_6.pages.inventory_page import InventoryPage
from HW_6.pages.login_page import LoginPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    # driver.implicitly_wait(20)
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()

def test_valid_username_valid_password(driver):
    login_page = LoginPage(driver)
    login_page.set_username("standard_user")
    login_page.set_password("secret_sauce")
    login_page.click_login_button()
    assert "inventory.html" in login_page.get_current_url(), ('Not')

    inventory_page = InventoryPage(driver)
    assert inventory_page.inventory_list_is_displayed()

def test_invalid_username_valid_password(driver):
    login_page = LoginPage(driver)
    login_page.set_username("serfererferrd_user")
    login_page.set_password("secret_sauce")
    login_page.click_login_button()

    assert login_page.error_box_is_displayed()
    assert "Username and password do not match any user in this service" in login_page.check_login_status()

def test_valid_username_invalid_password(driver):
    login_page = LoginPage(driver)
    login_page.set_username("standard_user")
    login_page.set_password("<xcv<dvsauce")
    login_page.click_login_button()

    assert login_page.error_box_is_displayed()
    assert "Username and password do not match any user in this service" in login_page.check_login_status()

def test_empty_username(driver):
    login_page = LoginPage(driver)
    login_page.set_username("")
    login_page.set_password("secret_sauce")
    login_page.click_login_button()

    assert login_page.error_box_is_displayed()
    assert "Username is required" in login_page.check_login_status()

def test_empty_password(driver):
    login_page = LoginPage(driver)
    login_page.set_username("standard_user")
    login_page.set_password("")
    login_page.click_login_button()

    assert login_page.error_box_is_displayed()
    assert "Password is required" in login_page.check_login_status()

def test_empty_username_empty_password(driver):
    login_page = LoginPage(driver)
    login_page.set_username("")
    login_page.set_password("")
    login_page.click_login_button()

    assert login_page.error_box_is_displayed()
    assert "Username is required" in login_page.check_login_status()


