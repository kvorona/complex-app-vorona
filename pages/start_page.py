from time import sleep

from selenium.webdriver.common.by import By

from constants.start_page import StartPageConstants
from pages.base_page import BasePage


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
        assert error_message.text == self.constants.SIGN_IN__ERROR_TEXT

    def sign_up(self, username='', email='', password=''):
        self.fill_field(xpath=self.constants.SIGN_UP_USERNAME, value=username)
        self.fill_field(xpath=self.constants.SIGN_UP_EMAIL, value=email)
        self.fill_field(xpath=self.constants.SIGN_UP_PASSWORD, value=password)
        # sleep(1)
        # self.click(xpath=self.constants.SIGN_UP_BUTTON)

    def find_elem_my_profile(self):
        assert self.driver.find_element(by=By.XPATH,
                                        value=self.constants.MY_PROFILE_BUTTON).is_displayed(), "Not found button 'My Profile'"

    def find_elem_create_post(self):
        assert self.driver.find_element(by=By.XPATH,
                                        value=self.constants.CREATE_POST).is_displayed(), "Not found button 'create-post'"

    # TODO: def find_elem_profile_name(self):
    #     assert self.driver.find_element(by=By.XPATH, value=f".//a[@href='/profile/{test_username}']").is_displayed()

    def click_sign_up_button(self):
        sleep(1)
        self.click(xpath=self.constants.SIGN_UP_BUTTON)

    def username_error(self):
        assert self.driver.find_element(by=By.XPATH, value=self.constants.SIGN_UP_USERNAME_ERROR).is_displayed(), \
            "Not see message 'Username must be at least 3 characters.'"

    def username_error_second(self):
        assert self.driver.find_element(by=By.XPATH, value=self.constants.SIGN_UP_USERNAME_ERROR2).is_displayed(), \
            "Not see message 'Username can only contain letters and numbers.'"

    def password_error(self):
        assert self.driver.find_element(by=By.XPATH, value=self.constants.SIGN_UP_PASSWORD_ERROR).is_displayed(), \
            "Password must be at least 12 characters."

    def email_error(self):
        assert self.driver.find_element(by=By.XPATH, value=self.constants.SIGN_UP_EMAIL_ERROR).is_displayed(), \
            "We not see message 'You must provide a valid email address'"

    def display_sign_up_button(self):
        assert self.driver.find_element(by=By.XPATH, value=self.constants.SIGN_UP_BUTTON).is_displayed(), \
            "We not see button 'Sign up for OurApp'"
