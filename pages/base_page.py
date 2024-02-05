from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_text(self, xpath):
        locator = (By.XPATH, xpath)
        element = self.driver.find_element(locator)
        return element.text

    def get_text_css(self, css):
        locator = (By.CSS_SELECTOR, css)
        element = self.driver.find_element(locator)
        return element.text

    def get_attribute(self, locator, attribute):
        element = self.driver.find_element(By.XPATH, locator)
        return element.get_attribute(attribute)

    def get_locator_xpath(self, locator):
        return self.driver.find_element(By.XPATH, locator)

    def click_on(self, locator):
        element = self.get_locator_xpath(locator)
        element.click()

    def get_locator_css(self, locator):
        return self.driver.find_element(By.CSS_SELECTOR, locator)

    def send_keys(self, locator, text):
        element = self.driver.find_element(By.XPATH, locator)
        element.send_keys(text)

    def clear_input(self, locator):
        element = self.driver.find_element(By.XPATH, locator)
        element.clear()

    def click_release(self, locator):
        element = self.driver.find_element(By.XPATH, locator)
        ActionChains(self.driver).click(element).perform()

    def double_click(self, locator):
        element = self.driver.find_element(By.XPATH, locator)
        ActionChains(self.driver).double_click(element).perform()

    def keyboard_click(self, locator):
        element = self.driver.find_element(By.XPATH, locator)
        ActionChains(self.driver).key_down(Keys.CONTROL).click(element).key_up(Keys.CONTROL).perform()

    def click_by_js(self, locator):
        element = self.driver.find_element(By.XPATH, locator)
        self.driver.execute_script("arguments[0].click();", element)

    def close_alert(self):
        alert = self.driver.switch_to.alert
        print(alert.text)
        alert.accept()

    def text_alert(self, text):
        promt = self.driver.switch_to.alert
        promt.send_keys(text)
        promt.accept()
