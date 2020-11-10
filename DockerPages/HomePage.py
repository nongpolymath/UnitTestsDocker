from selenium.webdriver.common.keys import Keys


class DockerHomePageLocators(object):

    def __init__(self, driver):
        self.driver = driver

    @property
    def page_title(self):
        return self.driver.title

    @property
    def search_button(self):
        return self.driver.find_element_by_id('searchToggle')

    @property
    def search_text_box(self):
        return self.driver.find_element_by_id('searchText')

    @property
    def sign_in(self):
        return self.driver.find_element_by_css_selector("a[href='http://hub.docker.com/sso/start']")

    @property
    def get_started_button(self):
        return self.driver.find_element_by_css_selector('a.btn')

    def click_search_button_and_enter_text(self, text):
        self.search_button.click()
        self.search_text_box.send_keys(text)
        self.search_text_box.send_keys(Keys.ENTER)

    def click_sign_in(self):
        self.sign_in.click()
