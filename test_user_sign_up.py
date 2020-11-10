import os, time
import unittest
import logging
import string, random
import HtmlTestRunner

from UnitTestsDocker.DockerPages.HomePage import DockerHomePageLocators
from UnitTestsDocker.DockerPages.SignInPage import SignInLocators
from UnitTestsDocker.test_base_home_page import DockerHomePageBaseTest


class UserSignupTest(DockerHomePageBaseTest):

    def test_sign_up_button_works(self):
        home_page = DockerHomePageLocators(self.driver)
        logging.info("User navigates to SignIn Page")
        home_page.click_sign_in()
        time.sleep(1)

        logging.info("User navigates to SignIn Page")
        sign_in_page = SignInLocators(self.driver)
        sign_in_page.click_sign_up_button()

    def generate_user_name(self):
