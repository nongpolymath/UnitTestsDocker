import os
import time
import unittest

import HtmlTestRunner

from UnitTestsDocker.DockerPages.HomePage import DockerHomePageLocators
from UnitTestsDocker.DockerPages.SignInPage import SignInLocators
from UnitTestsDocker.test_base_home_page import DockerHomePageBaseTest

USERNAME = 'dockerauto1'
PASSWORD = 'pythoncookbook12'


class LoginTest(DockerHomePageBaseTest):
    """Tests the login functionality of a registered user"""

    def test_sign_in_button_works(self):
        """tests the sign in button works on landing page"""
        home_page = DockerHomePageLocators(self.driver)
        home_page.click_sign_in()
        time.sleep(2)

    def test_sign_in_functionality(self):
        """tests the sign in functionality """
        sign_in_page = SignInLocators(self.driver)
        sign_in_page.enter_docker_id(USERNAME)
        sign_in_page.enter_user_password(PASSWORD)
        sign_in_page.click_sign_in_button()


if __name__ == "__main__":
    directoryPath = os.getcwd()
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=directoryPath + '//reports'))
