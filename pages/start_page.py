from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from constants.start_page import StartPageConstants
from pages.base_page import BasePage
from pages.utils import wait_until_ok, log_wrapper


class StartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = StartPageConstants()

    def sign_in(self, username='', password=''):
        self.fill_field(xpath=self.constants.SIGN_IN_USERNAME, value=username)
        self.fill_field(xpath=self.constants.SIGN_IN_PASSWORD, value=password)
        self.click(xpath=self.constants.SIGN_IN_BUTTON)

    def error_message(self):
        error_message = self.driver.find_element(by=By.XPATH, value=".//div[@class='alert alert-danger text-center']")
        assert error_message.text == "Invalid username / pasword", "Text is not valid"

    @log_wrapper
    def sign_up(self, username='', email='', password=''):
        """Sing up successfully"""
        self.fill_field(xpath=self.constants.SIGN_UP_USERNAME, value=username)
        self.fill_field(xpath=self.constants.SIGN_UP_EMAIL, value=email)
        self.fill_field(xpath=self.constants.SIGN_UP_PASSWORD, value=password)

    def find_elem_my_profile(self):
        self.is_display(self.constants.MY_PROFILE_BUTTON)

    def find_elem_create_post(self):
        self.is_display(self.constants.CREATE_POST)

    @wait_until_ok(timeout=7, period=1)
    def click_sign_up_button(self):
        self.wait_until_clickable(self.constants.SIGN_UP_BUTTON)
        self.find_and_click(self.constants.SIGN_UP_BUTTON)

    @wait_until_ok(timeout=10, period=1)
    def click_sign_up_and_verify(self):
        self.click(self.constants.SIGN_UP_BUTTON)
        assert not self.is_element_exists(self.constants.SIGN_UP_BUTTON)

    @log_wrapper
    def username_error(self):
        """You see username error"""
        self.is_display(self.constants.SIGN_UP_USERNAME_ERROR)

    def username_error_second(self):
        self.is_display(self.constants.SIGN_UP_USERNAME_ERROR2)

    @log_wrapper
    def password_error(self):
        """You see password error"""
        self.is_display(self.constants.SIGN_UP_PASSWORD_ERROR)

    @log_wrapper
    def email_error(self):
        """You see email error"""
        self.is_display(self.constants.SIGN_UP_EMAIL_ERROR)

    def display_sign_up_button(self):
        self.is_display(self.constants.SIGN_UP_BUTTON)

    def is_display(self, xpath):
        assert self.driver.find_element(by=By.XPATH, value=xpath).is_displayed()

    def is_element_exists(self, xpath):
        try:
            self.driver.find_element(by=By.XPATH, value=xpath)
            return True
        except (TimeoutError, NoSuchElementException):
            return False
