import unittest
import time, os
from selenium import webdriver
import HtmlTestRunner


class DockerHomePageBaseTest(unittest.TestCase):
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
    directoryPath = os.getcwd()
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=directoryPath+'//reports'))
