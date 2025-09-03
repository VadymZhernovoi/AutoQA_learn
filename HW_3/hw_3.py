"""
Написать автотест с использованием Python и Pytest, который:

1. Открывает https://itcareerhub.de/ru
2. Проверяет, что на странице отображаются:
    Логитип ITCareerHub
    Ссылка “Программы”
    Ссылка “Способы оплаты”
    Ссылка “Новости”
    Ссылка “О нас”
    Ссылка “Отзывы”
    Кнопки переключения языка (ru и de)
3. Кликнуть по иконке с телефонной трубкой
4. Проверить что текст “Если вы не дозвонились, заполните форму на сайте. Мы свяжемся с вами” отображается.
"""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://itcareerhub.de/ru")
    yield driver
    driver.quit()
"""

"""
def test_logo_is_displayed(driver):
    """
    Проверяет, что на странице отображаются Логoтип ITCareerHub
    """
    logo_img = driver.find_element(By.CSS_SELECTOR, ".tn-atom__img:nth-child(1)")
    assert logo_img.is_displayed() == True


def test_payments_is_displayed(driver):
    """
    Проверяет, что на странице отображаются Ссылка “Программы”
    """
    link_programs = driver.find_element(By.CSS_SELECTOR, ".t794__tm-link")
    assert link_programs.is_displayed() == True

def test_link_programs_is_displayed(driver):
    """
    Проверяет, что на странице отображаются Ссылка “Программы”
    """
    payments_link = driver.find_element(By.LINK_TEXT, "Способы оплаты")
    assert payments_link.is_displayed() == True

def test_link_news_is_displayed(driver):
    """
    Проверяет, что на странице отображаются Ссылка “Новости”
    """
    link_news = driver.find_element(By.LINK_TEXT, "Новости")
    assert link_news.is_displayed() == True

def test_link_about_is_displayed(driver):
    """
    Проверяет, что на странице отображаются Ссылка “О нас”
    """
    link_about = driver.find_element(By.LINK_TEXT, "О нас")
    assert link_about.is_displayed() == True

def test_link_reviews_is_displayed(driver):
    """
    Проверяет, что на странице отображаются Ссылка “Отзывы”
    """
    link_reviews = driver.find_element(By.LINK_TEXT, "Отзывы")
    assert link_reviews.is_displayed() == True

def test_button_language_ru_is_displayed(driver):
    """
    Проверяет, что на странице отображаются Ссылка “Отзывы”
    """
    button_language_ru = driver.find_element(By.LINK_TEXT, "ru")
    assert button_language_ru.is_displayed() == True

def test_button_language_de_is_displayed(driver):
    """
    Проверяет, что на странице отображаются Ссылка “Отзывы”
    """
    button_language_de = driver.find_element(By.LINK_TEXT, "de")
    assert button_language_de.is_displayed() == True

from time import sleep

def test_button_telefone_text_after_click(driver):
    """
    Кликнуть по иконке с телефонной трубкой
    Проверить что текст “Если вы не дозвонились, заполните форму на сайте. Мы свяжемся с вами” отображается.
    """
    button_telefone = driver.find_element(By.CSS_SELECTOR, ".tn-atom__img:nth-child(1)")
    button_telefone.click()
    sleep(5)
    button_telefone_text_after_click = driver.find_element(By.XPATH, "//*[contains(., 'Если вы не дозвонились, заполните форму на сайте. Мы свяжемся с вами')]")
    assert button_telefone_text_after_click.is_displayed() == True



