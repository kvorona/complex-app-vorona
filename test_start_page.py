import logging
import random

import pytest
from selenium.webdriver.chrome.webdriver import WebDriver

from constants.base import BaseConstants
from pages.start_page import StartPage


class TestStartPage:
    log = logging.getLogger("[StartPage]")

    @pytest.fixture(scope="function")
    def start_page(self):
        driver = WebDriver(executable_path=BaseConstants.DRIVER)
        driver.get(BaseConstants.BASE_URL)
        yield StartPage(driver)
        driver.close()

    def test_empty_fields_login(self, start_page):
        """
        - Create driver
        - Open start page
        - Clear field login
        - Clear field password
        - Click on 'Sign In' button
        - Verify error message
        """

        start_page.sign_in()
        self.log.info("Verifying error message")
        start_page.error_message()

    def test_invalid_login(self, start_page):
        """
        - Create driver
        - Open start page
        - Fill field login
        - Fill field password
        - Click on 'Sign In' button
        - Verify error message
        """
        start_page.sign_in(username='RandomName13', password='RandomPwd11')
        start_page.error_message()

    def test_registration_form_with_correct_values(self, start_page):
        """
        - Create driver
        - Open start page
        - Fill field Username
        - Fill field Email
        - Fill field Password
        - Click on 'Sign up for OurApp' button
        """

        start_page.sign_up(username=f"username{random.randint(0, 200)}",
                           password=f'RandomPwd11{random.randint(0, 200)}',
                           email=f"email{random.randint(0, 200)}@gmail.com")
        start_page.click_sign_up_button()

        start_page.find_elem_my_profile()
        start_page.find_elem_create_post()

        # TODO: username_field = driver.find_element(by=By.XPATH, value=".//input[@name='username'
        #  and @id='username-register']")
        # test_username = f"username{random.randint(0, 200)}"
        # username_field.send_keys(test_username)
        # start_page.find_elem_profile_name()

        # assert driver.find_element(by=By.XPATH, value=f".//a[@href='/profile/{test_username}']").is_displayed()

    def test_registration_form_required_fields(self, start_page):
        """
        - Create driver
        - Click on 'Sign up for OurApp' button
        """
        start_page.click_sign_up_button()

        start_page.username_error()
        start_page.password_error()
        start_page.email_error()

    def test_validation_username_field(self, start_page):
        """
        - Create driver
        - Open start page
        - Fill field invalid values for Username, like “####”
        - Fill field Email
        - Fill field Password
        - Click on 'Sign up for OurApp' button
        """

        start_page.sign_up(username="####", password=f'RandomPwd11{random.randint(0, 200)}',
                           email=f"email{random.randint(0, 200)}@gmail.com")
        start_page.click_sign_up_button()

        start_page.username_error_second()
        start_page.display_sign_up_button()

    def test_registration_with_only_username_field(self, start_page):
        """
        - Create driver
        - Open start page
        - Fill field Username
        - Click on 'Sign up for OurApp' button
        """
        start_page.sign_up(username=f"username{random.randint(0, 200)}")
        start_page.click_sign_up_button()

        start_page.display_sign_up_button()
        start_page.password_error()
        start_page.email_error()

        # TODO: assert not driver.find_element(by=By.XPATH,
        #  value=".//div[contains(text(),'Username can only contain letters and numbers.')]").is_displayed()

    def test_registration_with_only_email_field(self, start_page):
        """
        - Create driver
        - Open start page
        - Fill field email
        - Click on 'Sign up for OurApp' button
        """
        start_page.sign_up(email=f"email{random.randint(0, 200)}@gmail.com")
        start_page.click_sign_up_button()

        start_page.display_sign_up_button()
        start_page.username_error()
        start_page.password_error()

        # TODO: assert not driver.find_element(by=By.XPATH, value=".//div[contains(text(),
        #  'You must provide a valid email address.')]").is_displayed()

    def test_registration_with_only_password_field(self, start_page):
        """
        - Create driver
        - Open start page
        - Fill field password
        - Click on 'Sign up for OurApp' button
        """

        start_page.sign_up(password=f"Passwordtest{random.randint(0, 200)}")
        start_page.click_sign_up_button()

        start_page.display_sign_up_button()
        start_page.username_error()
        start_page.email_error()

        # TODO: assert not driver.find_element(by=By.XPATH, value=".//div[contains(text(),
        #  'Password must be at least 12 characters.')]").is_displayed(), "Password must be at least 12 characters."
