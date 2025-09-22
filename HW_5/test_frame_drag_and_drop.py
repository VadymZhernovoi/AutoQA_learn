import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    # driver.implicitly_wait(20)
    driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
    yield driver
    driver.quit()

def test_drag_and_drop(driver):
    wait = WebDriverWait(driver, 10)
    accept_button = wait.until(EC.visibility_of_element_located((By.XPATH, "(//p[@class='fc-button-label'])[1]")))
    accept_button.click()

    wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "iframe")))
    frames = driver.find_elements(By.TAG_NAME, "iframe")
    assert frames

    # найдём галерею
    is_gallery = False
    for frame in frames:
        driver.switch_to.default_content()
        # переключаемся по фреймам пока не найдём
        driver.switch_to.frame(frame)
        if driver.find_elements(By.CSS_SELECTOR, "#gallery li"):
            is_gallery = True
            break

    assert is_gallery

    # сохраним размеры галереи и корзины для последующего сравнения
    gallery = driver.find_elements(By.CSS_SELECTOR, "#gallery li")
    len_gallery = len(gallery)
    len_trash = len(driver.find_elements(By.CSS_SELECTOR, "#trash li"))

    # перетягиваем в корзину
    trash = driver.find_element(By.CSS_SELECTOR, "#trash")
    action = ActionChains(driver)
    action.drag_and_drop(gallery[0], trash).perform()

    # ждём, пока обновиться корзина (размер увеличится на 1)
    wait.until(lambda d: len(d.find_elements(By.CSS_SELECTOR, "#trash  li")) == len_trash + 1)

    updated_gallery = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#gallery li")))
    updated_trash =  wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#trash li")))
    # сравниваем длины галереи и корзины
    assert len(updated_gallery)  == len_gallery - 1
    assert len(updated_trash) == len_trash + 1

