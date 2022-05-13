from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, xpath):
        self.driver.find_element(by=By.XPATH, value=xpath).click()

    def fill_field(self, xpath, value):
        field = self.driver.find_element(by=By.XPATH, value=xpath)
        field.clear()
        field.send_keys(value)
