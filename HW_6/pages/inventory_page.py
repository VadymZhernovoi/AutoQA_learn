from selenium.webdriver.common.by import By

def convert_text_in_id(text):
    return '[data-test="add-to-cart-' + text.lower().replace(" ", "-") + '"]', '[data-test="remove-' + text.lower().replace(" ", "-") + '"]'


class InventoryPage:
    INVENTORY_LIST = (By.CLASS_NAME, "inventory_list")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    INVENTORY_CART = (By.CLASS_NAME, "shopping_cart_link")
    CART_BUTTON = (By.ID, "shopping_cart_container")

    def __init__(self, driver):
        self.driver = driver

    def inventory_list_is_displayed(self):
        return self.driver.find_element(*self.INVENTORY_LIST).is_displayed()

    def get_length_inventory_list(self):
        return len(self.driver.find_elements(*self.INVENTORY_ITEMS))

    def add_item(self, item: str):
        css_selector, css_remove = convert_text_in_id(item)
        self.driver.find_element(By.CSS_SELECTOR, css_selector).click()
        return self.driver.find_element(By.CSS_SELECTOR, css_remove).text

    def click_cart_button(self):
        self.driver.find_element(*self.CART_BUTTON).click()




