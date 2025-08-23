"""
Написать скрипт, который:
    Открывает в браузере Firefox https://itcareerhub.de/ru
    Переходит в раздел “Способы оплаты”
    Делает скриншот этой секции страницы
"""
from time import sleep
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture
def driver():
    # Инициализация WebDriver для Firefox
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    # Максимизация окна на всякий случай, чтобы все влезло на экран
    driver.maximize_window()
    # Передача драйвера в тест
    yield driver
    # Закрытие браузера
    driver.quit()


def test_screenshot_payment_methods_page(driver):
    # Открываем сайт itcareerhub.de/ru
    driver.get("https://itcareerhub.de/ru")

    # Находим раздел “Способы оплаты”
    about_link = driver.find_element(By.LINK_TEXT, "Способы оплаты")
    # Кликаем на “Способы оплаты”
    about_link.click()
    sleep(3)
    # делаем screenshot
    driver.save_screenshot("./itcareerhub_payment_methods.png")
