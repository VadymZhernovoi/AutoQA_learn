from selenium.webdriver.common.by import By

class CheckOutStepOne:
    FIRSTNAME_INPUT = (By.ID, "first-name")
    LASTNAME_INPUT = (By.ID, "last-name")
    ZIPCODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    ERROR_BOX = (By.CLASS_NAME, "error-message-container error")

    def __init__(self, driver):
        self.driver = driver

    def set_first_name(self, first_name_value: str):
        self.driver.find_element(*self.FIRSTNAME_INPUT).send_keys(first_name_value)

    def set_last_name(self, last_name_value: str):
        self.driver.find_element(*self.LASTNAME_INPUT).send_keys(last_name_value)

    def set_zipcode(self, zipcode_value: str):
        self.driver.find_element(*self.ZIPCODE_INPUT).send_keys(zipcode_value)

    def click_continue_button(self):
        self.driver.find_element(*self.CONTINUE_BUTTON).click()

    def error_box_is_not_displayed(self):
        return self.driver.find_element(*self.ERROR_BOX).is_displayed()




