import unittest
from selenium import webdriver
import HtmlTestRunner
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))


class DockerHomePageBaseTest(unittest.TestCase):
    """Base Test for browser app setup and teardown """

    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get("https://www.docker.com")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(3)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == "__main__":
    directoryPath = os.path.dirname(os.getcwd())
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=directoryPath+'//reports'))
