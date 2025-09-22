from selenium.webdriver.common.by import By

def convert_text_in_id(text):
    return '[data-test="add-to-cart-' + text.lower().replace(" ", "-") + '"]'

class CartPage:
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    CART_CHECKOUT = (By.ID, "checkout")
    CART_ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")

    def __init__(self, driver):
        self.driver = driver

    def get_length_cart_list(self):
        return len(self.driver.find_elements(*self.CART_ITEMS))

    def get_total_inventory_price(self):
        return self.driver.find_element(*self.CART_ITEM_PRICE).text

    def click_checkout(self):
        self.driver.find_element(*self.CART_CHECKOUT).click()




