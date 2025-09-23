from decimal import Decimal

from selenium.webdriver.common.by import By

class CheckOutStepTwo:
    SUMMARY_TOTAL = (By.CLASS_NAME, "summary_total_label")
    FINISH_BUTTON = (By.ID, "finish")

    def __init__(self, driver):
        self.driver = driver

    def get_summary_total(self):
        text = self.driver.find_element(*self.SUMMARY_TOTAL).text
        try:
            amount_str = text.split("$", 1)[1]
        except IndexError:
            raise AssertionError(f"Неверный формат summary_total: {text}")

        return Decimal(amount_str)

    def click_finish_button(self):
        self.driver.find_element(*self.FINISH_BUTTON).click()




