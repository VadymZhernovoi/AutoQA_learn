import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    # driver.implicitly_wait(20)
    driver.get("http://uitestingplayground.com/textinput")
    yield driver
    driver.quit()
"""
Задание 1: Проверка изменения текста кнопки
    Тестируемый сайт: http://uitestingplayground.com/textinput
    Шаги теста:
        Перейдите на сайт Text Input.
        Введите в поле ввода текст "ITCH".
        Нажмите на синюю кнопку.
        Проверьте, что текст кнопки изменился на "ITCH"."""
def test_change_text_button(driver):
    text_input = "ITCH"
    password_input_field = driver.find_element(By.CLASS_NAME, "form-control")
    password_input_field.send_keys(text_input)
    login_button = driver.find_element(By.CLASS_NAME, "btn-primary")
    login_button.click()
    result = driver.find_element(By.CLASS_NAME, "btn-primary")
    # sleep(5)
    assert result.text == text_input

"""
Задание 2: Проверка загрузки изображений
    Тестируемый сайт: https://bonigarcia.dev/selenium-webdriver-java/loading-images.html
    Шаги теста:
        Перейдите на сайт Loading Images.
        Дождитесь загрузки всех изображений.
        Получите значение атрибута alt у третьего изображения.
        Убедитесь, что значение атрибута alt равно "award".
"""
@pytest.fixture
def driver_2():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    # driver.implicitly_wait(20)
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
    yield driver
    driver.quit()

def test_img_is_loaded(driver_2):
    expected_text = "Done!"
    wait = WebDriverWait(driver_2, 20)
    wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "lead"), expected_text))
    result = driver_2.find_element(By.CLASS_NAME, "lead")
    assert result.text == expected_text
    attr = ("alt","award")
    result = driver_2.find_element(By.ID, attr[1])
    # sleep(5)
    assert result.get_attribute(attr[0]) == attr[1]
