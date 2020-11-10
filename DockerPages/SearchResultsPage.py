class SearchResultsLocators(object):

    def __init__(self, driver):
        self.driver = driver

    @property
    def search_results_header(self):
        return self.driver.find_element_by_css_selector('h2')

    @property
    def why_docker_text(self):
        return self.driver.find_element_by_link_text('Why Docker').text

    @property
    def get_started_with_docker_text(self):
        return self.driver.find_element_by_link_text('Get Started with Docker').text