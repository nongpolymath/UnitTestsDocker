import os, time
import unittest
import logging
import string, random
import HtmlTestRunner

from UnitTestsDocker.DockerPages.HomePage import DockerHomePageLocators
from UnitTestsDocker.DockerPages.SignInPage import SignInLocators
from UnitTestsDocker.test_base_home_page import DockerHomePageBaseTest

PASSWORD_STRENGTH = 8

class UserSignupTest(DockerHomePageBaseTest):

    def test_sign_up_button_works(self):
        home_page = DockerHomePageLocators(self.driver)
        logging.info("User navigates to SignIn Page")
        home_page.click_sign_in()
        time.sleep(1)

        logging.info("User navigates to SignIn Page")
        sign_in_page = SignInLocators(self.driver)
        sign_in_page.click_sign_up_button()

    @property
    def generate_user_name(self):
        return "dockerauto"+str(random.randint())

    @property
    def generate_password(self):
        return ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k=PASSWORD_STRENGTH))
