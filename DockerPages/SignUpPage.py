class SignUpLocators(object):
    """POM class for Signup Page"""

    def __init__(self, driver):
        self.driver = driver

    @property
    def sign_up_text(self):
        return self.driver.find_element_by_css_selector(".styles__mainTitle___3_abT")

    @property
    def user_id(self):
        return self.driver.find_element_by_id("username")

    @property
    def email(self):
        return self.driver.find_element_by_id('email')

    @property
    def password(self):
        return self.driver.find_element_by_id('password')

    @property
    def captcha_checkbox(self):
        return self.driver.find_element_by_id("recaptcha-anchor")

    @property
    def sign_up_button(self):
        return self.driver.find_element_by_class_name('styles__signUpButton___jEpn5')

    def enter_new_docker_id(self, user_text):
        user_id = self.user_id
        user_id.send_keys(user_text)

    def enter_user_password(self, user_password):
        self.password.click()
        self.password.send_keys(user_password)

    def enter_user_email(self, email_id):
        self.email.click()
        self.email.send_keys(email_id)

    def click_captcha_checkbox(self):
        self.captcha_checkbox.click()

    def click_sign_up_button(self):
        self.sign_up_button.click()
