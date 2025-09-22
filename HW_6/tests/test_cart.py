import pytest
from time import sleep
from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from HW_6.pages.cart_page import CartPage
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

def test_check_6_items(driver):
    login_page = LoginPage(driver)
    login_page.set_username("standard_user")
    login_page.set_password("secret_sauce")
    login_page.click_login_button()
    assert "inventory.html" in login_page.get_current_url(), ('Not...')

    inventory_page = InventoryPage(driver)
    assert inventory_page.inventory_list_is_displayed()

    inventory_page = InventoryPage(driver)
    assert inventory_page.get_length_inventory_list() == 6

    items = ["Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie"]
    for item in items:
        inventory_page.add_item(item)

    inventory_page.click_cart_button()
    assert "cart.html" in login_page.get_current_url(), ('Not...')

    cart_page = CartPage(driver)
    #assert cart_page.get_length_cart_list() == 3

    print('cart_page.item_prices', cart_page.get_backpack_price())

