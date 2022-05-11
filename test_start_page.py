import logging
import random
from time import sleep

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class TestStartPage:
    log = logging.getLogger("[StartPage]")

    def test_empty_fields_login(self):
        """
        - Create driver
        - Open start page
        - Clear field login
        - Clear field password
        - Click on 'Sign In' button
        - Verify error message
        """
        # Create driver
        # driver = WebDriver(executable_path="chromedriver")
        driver = WebDriver(executable_path="/Users/katyahrynchyshyna/PycharmProjects/complex-app_vorona/chromedriver")

        # Open start page
        self.log.info("Opening start page")
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")

        # Clear field login
        self.log.info("Cleaning login field")
        # - Find element
        login_field = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Username']")
        # - Clear
        login_field.clear()

        # Clear field password
        self.log.info("Cleaning password field")
        # - Find element
        password_field = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Password']")
        # - Clear
        password_field.clear()

        # Click on 'Sign In' button
        self.log.info("Going to click 'Sign In' button")
        driver.find_element(by=By.XPATH, value=".//button[text()='Sign In']").click()

        # Verify error message
        self.log.info("Verifying error message")
        error_message = driver.find_element(by=By.XPATH, value=".//div[@class='alert alert-danger text-center']")
        assert error_message.text == "Invalid username / password", "Text is not valid"

        # Close driver
        driver.close()

    def test_invalid_login(self):
        """
        - Create driver
        - Open start page
        - Fill field login
        - Fill field password
        - Click on 'Sign In' button
        - Verify error message
        """
        # Create driver
        driver = WebDriver(executable_path="/Users/katyahrynchyshyna/PycharmProjects/complex-app_vorona/chromedriver")

        # Open start page
        self.log.info("Opening start page")
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")

        # Clear field login
        self.log.info("Filling login field")
        # - Find element
        login_field = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Username']")
        # - Clear
        login_field.clear()
        # - Fill
        login_field.send_keys("RandomName13")
        sleep(1)

        # Clear field password
        self.log.info("Filling password field")
        # - Find element
        password_field = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Password']")
        # - Clear
        password_field.clear()
        # - Fill
        password_field.send_keys("RandomPwd11")
        sleep(1)

        # Click on 'Sign In' button
        self.log.info("Going to click 'Sign In' button")
        driver.find_element(by=By.XPATH, value=".//button[text()='Sign In']").click()
        sleep(1)

        # Verify error message
        self.log.info("Verifying error message")
        error_message = driver.find_element(by=By.XPATH, value=".//div[@class='alert alert-danger text-center']")
        assert error_message.text == "Invalid username / password", "Text is not valid"

        # Close driver
        driver.close()

    log = logging.getLogger("[Registration form]")

    def test_registration_form_with_correct_values(self):
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

        self.log.info("WE can see button 'create-post'")
        self.log.info("User successfully authorized!")

        self.log.info("Close driver")
        driver.close()

    def test_registration_form_required_fields(self):
        """
        - Create driver
        - Click on 'Sign up for OurApp' button
        """
        driver = WebDriver(executable_path="/Users/katyahrynchyshyna/PycharmProjects/complex-app_vorona/chromedriver")

        self.log.info("Opening start page")
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        sleep(1)

        self.log.info("Going to click 'Sign up for OurApp' button")
        driver.find_element(by=By.XPATH, value='.//button[contains(text(),"Sign up for OurApp")]').click()
        sleep(1)

        assert driver.find_element(by=By.XPATH,
                                   value=".//div[contains(text(),'Username must be at least 3 characters.')]").is_displayed(), \
            "Not see message 'Username must be at least 3 characters.'"
        self.log.info("WE can see info message 'Username must be at least 3 characters'")
        assert driver.find_element(by=By.XPATH,
                                   value=".//div[contains(text(),'You must provide a valid email address.')]").is_displayed(), \
            "We not see message 'You must provide a valid email address'"
        self.log.info("WE can see info message 'You must provide a valid email address'")
        assert driver.find_element(by=By.XPATH,
                                   value=".//div[contains(text(),'Password must be at least 12 characters.')]").is_displayed(), \
            "Password must be at least 12 characters."
        self.log.info("WE can see info message 'Password must be at least 12 characters.'")

        self.log.info("Fields: name, password and email are required for registration!")

        self.log.info("Close driver")
        driver.close()

    def test_validation_username_field(self):
        """
        - Create driver
        - Open start page
        - Fill field invalid values for Username, like “####”
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
        username_field.send_keys("####")
        sleep(1)
        assert driver.find_element(by=By.XPATH,
                                   value=".//div[contains(text(),'Username can only contain letters and numbers.')]").is_displayed(), \
            "Not see message 'Username can only contain letters and numbers.'"
        self.log.info("WE can see info message 'Username can only contain letters and numbers'")

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
                                   value=".//div[contains(text(),'Username can only contain letters and numbers.')]").is_displayed(), \
            "Not see message 'Username can only contain letters and numbers.'"
        self.log.info(
            "We can see info message 'Username can only contain letters and numbers.' after click on a button")
        assert driver.find_element(by=By.XPATH,
                                   value='.//button[contains(text(),"Sign up for OurApp")]').is_displayed(), \
            "We not see button 'Sign up for OurApp'"
        self.log.info("We see button 'Sign up for OurApp'")

        self.log.info("Close driver")
        driver.close()

    def test_registration_with_only_username_field(self):
        """
        - Create driver
        - Open start page
        - Fill field Username
        - Click on 'Sign up for OurApp' button
        """
        driver = WebDriver(executable_path="/Users/katyahrynchyshyna/PycharmProjects/complex-app_vorona/chromedriver")

        self.log.info("Opening start page")
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")

        self.log.info("Filling Username field")

        username_field = driver.find_element(by=By.XPATH,
                                             value=".//input[@name='username' and @id='username-register']")
        username_field.send_keys(f"username{random.randint(0, 200)}")
        sleep(1)

        self.log.info("Going to click 'Sign up for OurApp' button")
        driver.find_element(by=By.XPATH, value='.//button[contains(text(),"Sign up for OurApp")]').click()
        sleep(1)

        # TODO: assert not driver.find_element(by=By.XPATH,
        #                            value=".//div[contains(text(),'Username can only contain letters and numbers.')]").is_displayed()
        # sleep(1)

        assert driver.find_element(by=By.XPATH,
                                   value=".//div[contains(text(),'You must provide a valid email address.')]").is_displayed(), \
            "We not see message 'You must provide a valid email address'"
        self.log.info("WE can see info message 'You must provide a valid email address'")
        assert driver.find_element(by=By.XPATH,
                                   value=".//div[contains(text(),'Password must be at least 12 characters.')]").is_displayed(), \
            "Password must be at least 12 characters."
        self.log.info("WE can see info message 'Password must be at least 12 characters.'")
        assert driver.find_element(by=By.XPATH,
                                   value='.//button[contains(text(),"Sign up for OurApp")]').is_displayed(), \
            "We not see button 'Sign up for OurApp'"
        self.log.info("We see button 'Sign up for OurApp'")

        self.log.info("Close driver")
        driver.close()

    def test_registration_with_only_email_field(self):
        """
        - Create driver
        - Open start page
        - Fill field email
        - Click on 'Sign up for OurApp' button
        """
        driver = WebDriver(executable_path="/Users/katyahrynchyshyna/PycharmProjects/complex-app_vorona/chromedriver")

        self.log.info("Opening start page")
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")

        self.log.info("Filling Email field")
        email_field = driver.find_element(by=By.XPATH, value=".//input[@name='email']")
        email_field.send_keys(f"email{random.randint(0, 200)}@gmail.com")
        sleep(1)

        self.log.info("Going to click 'Sign up for OurApp' button")
        driver.find_element(by=By.XPATH, value='.//button[contains(text(),"Sign up for OurApp")]').click()
        sleep(1)

        # TODO: assert not driver.find_element(by=By.XPATH,
        #                            value=".//div[contains(text(),'You must provide a valid email address.')]").is_displayed()
        sleep(1)

        assert driver.find_element(by=By.XPATH,
                                   value=".//div[contains(text(),'Username must be at least 3 characters.')]").is_displayed(), \
            "Not see message 'Username must be at least 3 characters.'"
        assert driver.find_element(by=By.XPATH,
                                   value=".//div[contains(text(),'Password must be at least 12 characters.')]").is_displayed(), \
            "Password must be at least 12 characters."

        assert driver.find_element(by=By.XPATH,
                                   value='.//button[contains(text(),"Sign up for OurApp")]').is_displayed(), \
            "We not see button 'Sign up for OurApp'"
        self.log.info("We cannot registration. We see button 'Sign up for OurApp'")

        self.log.info("Close driver")
        driver.close()

    def test_registration_with_only_password_field(self):
        """
        - Create driver
        - Open start page
        - Fill field password
        - Click on 'Sign up for OurApp' button
        """
        driver = WebDriver(executable_path="/Users/katyahrynchyshyna/PycharmProjects/complex-app_vorona/chromedriver")

        self.log.info("Opening start page")
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")

        self.log.info("Filling password field")
        password_registration_field = driver.find_element(by=By.XPATH, value=".//input[@id='password-register']")
        password_registration_field.send_keys(f"Passwordtest{random.randint(0, 200)}")
        sleep(1)

        self.log.info("Going to click 'Sign up for OurApp' button")
        driver.find_element(by=By.XPATH, value='.//button[contains(text(),"Sign up for OurApp")]').click()
        sleep(1)

        assert driver.find_element(by=By.XPATH,
                                   value=".//div[contains(text(),'Username must be at least 3 characters.')]").is_displayed(), \
            "Not see message 'Username must be at least 3 characters.'"
        assert driver.find_element(by=By.XPATH,
                                   value=".//div[contains(text(),'You must provide a valid email address.')]").is_displayed(), \
            "We not see message 'You must provide a valid email address'"

        # TODO: assert not driver.find_element(by=By.XPATH,
        #                            value=".//div[contains(text(),'Password must be at least 12 characters.')]").is_displayed(), \
        #     "Password must be at least 12 characters."

        self.log.info("Close driver")
        driver.close()
