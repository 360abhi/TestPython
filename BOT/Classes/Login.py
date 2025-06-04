
import time
from BOT.utils.paths import Path_Utils

class Login:

    username_field = "//input[@name='username']"
    password_field = "//input[@name='password']"
    login_button = "(//div[.='Log in'])[last()]"
    skip = "(//div[.='Not now'])[last()]"

    def __init__(self,driver):
        self.driver = driver
        self.paths = Path_Utils(self.driver)

    def login(self,username,password):
        self.paths.send_keys_xpath(self.username_field,username)
        self.paths.send_keys_xpath(self.password_field,password)
        self.paths.click_xpath(self.login_button)
        time.sleep(5)
        self.paths.click_xpath(self.skip)
        

        