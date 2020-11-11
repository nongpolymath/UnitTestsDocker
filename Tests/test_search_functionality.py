import os
import sys
import time
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))

import HtmlTestRunner

from UnitTestsDocker.DockerPages.HomePage import DockerHomePageLocators
from UnitTestsDocker.DockerPages.SearchResultsPage import SearchResultsLocators
from UnitTestsDocker.Tests.test_base_home_page import DockerHomePageBaseTest

HOME_PAGE_TITLE = "Empowering App Development for Developers | Docker"
SEARCH_TEXT = "docker"
HEADER_TEXT = "Search results"
SEARCH_RESULT1 = 'Why Docker'
SEARCH_RESULT2 = "Get Started with Docker"


class SearchFunctionTest(DockerHomePageBaseTest):

    def test_search_functionality(self):
        """Tests Home Page title and search functionality with text as input works"""

        docker_home_page = DockerHomePageLocators(self.driver)
        self.assertEqual(HOME_PAGE_TITLE, docker_home_page.page_title,
                         "Search Results title should be correct")
        docker_home_page.click_search_button_and_enter_text(text=SEARCH_TEXT)
        time.sleep(2)

    def test_search_results_for_docker(self):
        """tests the indexed search results for query text 'docker'"""

        search_page_object = SearchResultsLocators(self.driver)
        self.assertEqual(HEADER_TEXT, search_page_object.search_results_header.text,
                         "Search Results title should be correct")
        self.assertEqual(SEARCH_RESULT1, search_page_object.why_docker_text,
                         "1st indexed search result should be correct")
        self.assertEqual(SEARCH_RESULT2, search_page_object.get_started_with_docker_text,
                         "2nd indexed search result should be correct")


if __name__ == "__main__":
    directoryPath = os.path.dirname(os.getcwd())
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=directoryPath + '//reports'))
