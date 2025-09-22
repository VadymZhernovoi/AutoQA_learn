from selenium.webdriver.common.by import By

class LoginPage:
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_BOX = (By.TAG_NAME, "h3")

    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username_value: str):
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username_value)

    def set_password(self, password_value: str):
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password_value)

    def click_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def get_current_url(self):
        return self.driver.current_url

    def error_box_is_displayed(self):
        return self.driver.find_element(*self.ERROR_BOX).is_displayed()

    def check_login_status(self):
        return self.driver.find_element(*self.ERROR_BOX).text
