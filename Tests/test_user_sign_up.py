import os
import sys
import unittest
import logging
import string
import random
import HtmlTestRunner

sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))

from UnitTestsDocker.DockerPages.HomePage import DockerHomePageLocators
from UnitTestsDocker.DockerPages.SignInPage import SignInLocators
from UnitTestsDocker.DockerPages.SignUpPage import SignUpLocators
from UnitTestsDocker.Tests.test_base_home_page import DockerHomePageBaseTest

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

PASSWORD_STRENGTH = 10


class UserSignupTest(DockerHomePageBaseTest):

    def test_button_sign_up_works(self):
        """Tests the User sign up UI flow and functionality from landing page till Submit.
            Explicit waits added for unexpected page load times
            """

        home_page_ob = DockerHomePageLocators(self.driver)
        logging.info("User navigates to SignIn Page")
        self.wait_for_clickable_ready(css_element="a[href='http://hub.docker.com/sso/start']")
        home_page_ob.click_sign_in()
        sign_in_page = SignInLocators(self.driver)
        self.wait_for_clickable_ready(css_element="a[href='https://hub.docker.com/signup']")
        sign_in_page.click_sign_up_button()
        logging.info("User is on SignUp Page")
        self.wait_for_page_to_load_title(class_name="styles__mainTitle___3_abT", text="Create a Docker ID.")
        name = generate_user_name()
        signup = SignUpLocators(self.driver)
        self.wait_for_user_id_to_load()
        signup.enter_new_docker_id(name)
        signup.enter_user_email(generate_email())
        signup.enter_user_password(generate_password())

        WebDriverWait(self.driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//*["
                                                                                                  "@id='signupForm"
                                                                                                  "']/div["
                                                                                                  "4]/div/div/div/div"
                                                                                                  "/div/iframe")))

        self.click_recaptcha()
        self.driver.switch_to.default_content()
        signup.click_sign_up_button()

    def wait_for_page_to_load_title(self, class_name, text):
        """
        generic function to explicitly wait for page title
        :param class_name: string
        :param text: string
        """

        try:
            WebDriverWait(self.driver, 10).until(
                EC.text_to_be_present_in_element((By.CLASS_NAME, class_name),
                                                 text))
        except TimeoutException:
            logging.error("Timed out waiting for page to load")
        finally:
            logging.info("Page loaded")

    def wait_for_user_id_to_load(self):
        """
        explicit wait function for user id to load on signup page
        """

        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@id='username']")))
        except TimeoutException:
            logging.error("Timed out waiting for user id to load")
        finally:
            logging.info("user id found")

    def wait_for_clickable_ready(self, css_element=None, xpath=None, clickable_id=None):
        """
        generic function to explicitly wait element is clickable by xpath , id or css
        :param clickable_id: string
        :param xpath: string
        :param css_element: string
        """

        try:
            if css_element:
                WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, css_element)))
            elif xpath:
                WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, xpath)))
            else:
                WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.ID, clickable_id)))

        except TimeoutException:
            logging.error("Timed out waiting for clickable ready")
        finally:
            logging.info("Ready to click")

    def click_recaptcha(self):
        """function to click on elements exist on separate iframes"""

        captcha = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "recaptcha-anchor")))
        captcha.click()

def generate_user_name():
    """random user name generator"""

    return "dockets" + str(random.randint(3, 200))


def generate_password():
    """random password generator"""

    return ''.join(random.choices(string.ascii_uppercase +
                                  string.digits, k=PASSWORD_STRENGTH))


def generate_email():
    """random email generator"""

    first = ''.join(random.choices(string.ascii_uppercase +
                                   string.digits, k=5))
    last = ''.join(random.choices(string.ascii_uppercase +
                                  string.digits, k=PASSWORD_STRENGTH))
    return first + last + "@yahoo.com"


if __name__ == "__main__":
    directoryPath = os.path.dirname(os.getcwd())
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=directoryPath + '//reports'))
