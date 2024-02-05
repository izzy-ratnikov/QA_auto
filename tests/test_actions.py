import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
import time

from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from pages.base_page import BasePage


@pytest.fixture(scope='session', autouse=False)
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


"""H/T Selenium Advanced"""


def test_for_check(driver):
    '''ввод текста, очистка текста, обычный клик'''

    driver.get("https://animego.org/")
    locator = "/html/body/div[2]/header/nav/div/div/ul[2]/li[3]/div/form/div/div/input"
    l_2 = '//*[@id="navbar-search"]'
    base_page = BasePage(driver)
    base_page.click_on(l_2)
    base_page.send_keys(locator, "Магическая битва 2")
    base_page.clear_input(locator)
    base_page.send_keys(locator, "Магическая битва")
    base_page.send_keys(locator, Keys.RETURN)
    assert driver.current_url == "https://animego.org/search/all?q=%D0%9C%D0%B0%D0%B3%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F+%D0%B1%D0%B8%D1%82%D0%B2%D0%B0"


def test_click_release(driver):
    '''клик с помощью мыши'''
    driver.get("https://animego.org/")
    locator = "/html/body/div[2]/header/nav/div/div/ul[1]/li[1]/a"
    l_2 = "/html/body/div[2]/header/nav/div/div/ul[1]/li[2]/a"
    base_page = BasePage(driver)
    base_page.click_release(locator)
    base_page.double_click(l_2)
    assert driver.current_url == "https://animego.org/manga"


def test_keyboard_click(driver):
    '''клик с помощью клавиатуры'''
    driver.get("https://animego.org/")
    locator = "/html/body/div[2]/header/nav/div/div/ul[1]/li[1]/a"
    base_page = BasePage(driver)
    base_page.keyboard_click(locator)
    windows = driver.window_handles
    driver.switch_to.window(windows[1])
    assert driver.current_url == "https://animego.org/anime"


def test_js_click(driver):
    """клик с помощью js"""
    driver.get("https://animego.org/")
    locator = "/html/body/div[2]/header/nav/div/div/ul[1]/li[3]/a"
    base_page = BasePage(driver)
    base_page.click_by_js(locator)
    assert driver.current_url == "https://animego.org/characters"


"""Работа с Alert"""

@pytest.mark.xfail(reason="InvalidArgumentException: Message: invalid argument: 'using' must be a string")

def test_close_alert(driver):
    driver.get("http://the-internet.herokuapp.com/javascript_alerts")
    locator = "//*[@id='content']/div/ul/li[1]/button"
    base_page = BasePage(driver)
    base_page.click_on(locator)
    base_page.close_alert()
    locato = "//*[@id='result']"
    assert "You successfully clicked an alert" == base_page.get_text(locato)


def test_name_alert(driver):
    driver.get("https://learn.javascript.ru/task/simple-page")
    locator = '/html/body/div[1]/div[2]/div/main/div[2]/div[2]/div[2]/div[1]/p[2]/a'
    base_page = BasePage(driver)
    base_page.click_on(locator)
    promt = driver.switch_to.alert
    promt.send_keys("Vlad")
    time.sleep(3)
    promt.accept()
    time.sleep(3)



"""Окна и вкладки, Iframe"""

def test_window(driver):
    driver.get("https://animego.org/")
    base_page = BasePage(driver)
    main_window = driver.current_window_handle
    base_page.keyboard_click("/html/body/div[2]/header/nav/div/div/ul[1]/li[1]/a")
    page_two = driver.current_window_handle
    windows = driver.window_handles
    driver.switch_to.window(windows[0])
    driver.close()
    driver.switch_to.window(windows[1])
    assert driver.current_url == "https://animego.org/anime"


@pytest.mark.xfail(reason="fixing")
def test_iframe(driver):
    driver.get("http://the-internet.herokuapp.com/iframe")
    driver.switch_to.frame(driver.find_elements(By.XPATH, "//iframe")[0])
    locator = "//*[@id='tinymce']/p"
    base_page = BasePage(driver)
    assert "Your content goes here." == base_page.get_text(locator)


"""Загрузка файлов"""

def test_load(driver):
    driver.get("https://yandex.by/")
    base_page = BasePage(driver)
    base_page.send_keys("//*[@id='image_search']", "C:/Users/IdeaPad 5/PycharmProjects/QA_auto/img/image.jpg")
    assert True

