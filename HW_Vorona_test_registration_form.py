import logging
import random
from time import sleep

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class TestStartPage:
    log = logging.getLogger("[StartPage]")

    def test_registration_form(self):
        """
        - Create driver
        - Open start page
        - Fill field Username
        - Fill field Email
        - Fill field Password
        - Click on 'Sign up for OurApp' button
        """
        driver = WebDriver(executable_path="/Users/katyahrynchyshyna/PycharmProjects/complex-app_vorona/chromedriver")

        self.log.info("Opening start page")
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")

        self.log.info("Filling Username field")

        username_field = driver.find_element(by=By.XPATH,
                                             value=".//input[@name='username' and @id='username-register']")
        test_username = f"username{random.randint(0, 200)}"
        username_field.send_keys(test_username)

        sleep(1)

        self.log.info("Filling Email field")
        email_field = driver.find_element(by=By.XPATH, value=".//input[@name='email']")
        email_field.send_keys(f"email{random.randint(0, 200)}@gmail.com")
        sleep(1)

        password_registration_field = driver.find_element(by=By.XPATH, value=".//input[@id='password-register']")
        password_registration_field.send_keys(f"Passwordtest{random.randint(0, 200)}")
        sleep(1)

        self.log.info("Going to click 'Sign up for OurApp' button")
        driver.find_element(by=By.XPATH, value='.//button[contains(text(),"Sign up for OurApp")]').click()
        sleep(1)

        assert driver.find_element(by=By.XPATH,
                                   value=".//img[@data-original-title='My Profile']").is_displayed(), \
            "Not found button 'My Profile'"
        self.log.info("WE can see button 'My Profile'")
        assert driver.find_element(by=By.XPATH, value=".//a[@href='/create-post']").is_displayed(), \
            "Not found button 'create-post'"
        assert driver.find_element(by=By.XPATH, value=f".//a[@href='/profile/{test_username}']").is_displayed()

        self.log.info("WE can see button 'create-pos'")
        self.log.info("User successfully authorized!")

        self.log.info("Close driver")
        driver.close()
