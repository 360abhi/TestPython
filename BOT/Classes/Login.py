
import time
from BOT.utils.paths import Path_Utils

class Login:

    username_field = "//input[@name='username']"
    password_field = "//input[@name='password']"
    login_button = "(//div[.='Log in'])[last()]"
    skip = "(//div[.='Not now'])[last()]"

    def __init__(self,driver,logger):
        self.logger = logger
        self.driver = driver
        self.paths = Path_Utils(self.driver)

    def log_action(self,action_result,success_msg,error_msg,capture_error=None,capture_locator=None):
        if action_result:
            self.logger.info(success_msg)
        else:
            self.logger.error(error_msg)
            raise Exception(error_msg)

    def login(self,username,password):
        self.log_action(self.paths.send_keys_xpath(self.username_field,username),
                        f"{username} entered successfully",
                        f"{username} enter exception")
        
        self.log_action(self.paths.send_keys_xpath(self.password_field,password),
                        f"Password enter success",
                        f"Password enter exception")
        
        self.log_action(self.paths.click_xpath(self.login_button),
                        "Login click success",
                        "Login click exception")

        self.log_action(self.paths.click_xpath(self.skip),
                        "Skip Save Info Success",
                        "Skip Save Info Exception")
        
        