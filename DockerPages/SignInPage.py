class SignInLocators(object):
    """POM class for SignIn Page"""

    def __init__(self, driver):
        self.driver = driver

    @property
    def docker_id(self):
        return self.driver.find_element_by_id('nw_username')

    @property
    def password(self):
        return self.driver.find_element_by_id('nw_password')

    @property
    def sign_in_button(self):
        return self.driver.find_element_by_id('nw_submit')

    @property
    def sign_up_button(self):
        return self.driver.find_element_by_css_selector("a[href='https://hub.docker.com/signup']")

    def enter_docker_id(self, user_id):
        self.docker_id.send_keys(user_id)

    def enter_user_password(self, user_password):
        self.password.send_keys(user_password)

    def click_sign_in_button(self):
        self.sign_in_button.click()

    def click_sign_up_button(self):
        self.sign_up_button.click()
