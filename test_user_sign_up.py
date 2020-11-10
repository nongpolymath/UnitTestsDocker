import os, time
import unittest
import logging
import string, random
import HtmlTestRunner

from UnitTestsDocker.DockerPages.HomePage import DockerHomePageLocators
from UnitTestsDocker.DockerPages.SignInPage import SignInLocators
from UnitTestsDocker.DockerPages.SignUpPage import SignUpLocators
from UnitTestsDocker.test_base_home_page import DockerHomePageBaseTest

PASSWORD_STRENGTH = 8


class UserSignupTest(DockerHomePageBaseTest):

    @property
    def generate_user_name(self):
        return "dockerauto" + str(random.randint(3, 200))

    @property
    def generate_password(self):
        return ''.join(random.choices(string.ascii_uppercase +
                                      string.digits, k=PASSWORD_STRENGTH))

    @property
    def generate_email(self):
        first = ''.join(random.choices(string.ascii_uppercase +
                                       string.digits, k=5))
        last = ''.join(random.choices(string.ascii_uppercase +
                                      string.digits, k=PASSWORD_STRENGTH))
        return first + last + "@aol.com"

    def test_sign_up_button_works(self):
        home_page = DockerHomePageLocators(self.driver)
        logging.info("User navigates to SignIn Page")
        home_page.click_sign_in()
        time.sleep(3)

        sign_in_page = SignInLocators(self.driver)
        sign_in_page.click_sign_up_button()
        time.sleep(2)

    def frame_switch(self, name):
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC

        WebDriverWait(self.driver, 6).until(EC.frame_to_be_available_and_switch_to_it((By.NAME, name)))

        #iframe = self.driver.find_element_by_css_selector(name)
        # self.driver.switch_to.frame(iframe)

    def test_new_user_sign_up(self):
        signup = SignUpLocators(self.driver)
        name = self.generate_user_name
        self.frame_switch("a-374tuuxvgphu")

        signup.enter_new_docker_id(name)
        # email_id = self.generate_email
        # signupForm
        # signup.enter_user_email(email_id)


        # signup_page.enter_user_email(self.generate_email)
        # signup_page.enter_user_password(self.generate_password)
        # signup_page.click_captcha_checkbox()
        # signup_page.click_sign_up_button()
        # time.sleep(1)


if __name__ == "__main__":
    directoryPath = os.getcwd()
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=directoryPath + '//reports'))
