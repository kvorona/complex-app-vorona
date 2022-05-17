from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.utils import wait_until_ok


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.waiter = WebDriverWait(driver=driver, timeout=5)

    def click(self, xpath):
        self.driver.find_element(by=By.XPATH, value=xpath).click()

    def fill_field(self, xpath, value):
        field = self.driver.find_element(by=By.XPATH, value=xpath)
        field.clear()
        field.send_keys(value)

    def wait_until_clickable(self, xpath):
        """Waits until element is clickable"""
        return self.waiter.until(method=expected_conditions.element_to_be_clickable((By.XPATH, xpath)))

    @wait_until_ok(timeout=7, period=1)
    def find_and_click(self, xpath):
        self.wait_until_clickable(xpath).click()
