import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import time
from webdriver_manager.chrome import ChromeDriverManager
from pages.base_page import BasePage


@pytest.fixture(scope='session', autouse=False)
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


def test_for_check(driver):
    '''ввод текста, очистка текста, обычный клик'''

    driver.get("https://animego.org/")
    locator = "/html/body/div[2]/header/nav/div/div/ul[2]/li[3]/div/form/div/div/input"
    l_2 = '//*[@id="navbar-search"]'
    base_page = BasePage(driver)
    base_page.click_on(l_2)
    base_page.send_keys(locator, "Магическая битва")
    time.sleep(5)
    base_page.clear_input(locator)
    time.sleep(5)

def test_click_release(driver):
    '''клик с помощью мыши'''
    driver.get("https://animego.org/")
    locator = "/html/body/div[2]/header/nav/div/div/ul[1]/li[1]/a"
    l_2 = "/html/body/div[2]/header/nav/div/div/ul[1]/li[2]/a"
    base_page = BasePage(driver)
    base_page.click_release(locator)
    time.sleep(4)
    base_page.double_click(l_2)
    time.sleep(4)

def test_keyboard_click(driver):
    '''клик с помощью клавиатуры'''
    driver.get("https://animego.org/")
    locator = "/html/body/div[2]/header/nav/div/div/ul[1]/li[1]/a"
    base_page = BasePage(driver)
    base_page.double_click(locator)
    time.sleep(4)

def test_js_click(driver):
    driver.get("https://animego.org/")
    locator = "/html/body/div[2]/header/nav/div/div/ul[1]/li[1]/a"
    base_page = BasePage(driver)
    base_page.click_by_js(locator)
    time.sleep(4)


