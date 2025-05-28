import os
import sys
from Selenium.utils.paths import Path_Utils


class Login:

    # Xpaths
    user_field = "//input[@id='user-name']"
    password_field = "//input[@id='password']"
    submit_button = "//input[@id='login-button']"
    error_msg = "//h3"
    success_product_tag = "//div[@id='inventory_filter_container']/div"

    def __init__(self,driver,logger):
        self.driver = driver
        self.paths = Path_Utils(self.driver)
        self.logger = logger


    def enterUsername(self,username):
        if self.paths.send_keys_xpath(self.user_field,text=username):
            self.logger.info("Username Entered Success")
        else:
            self.logger.error(f"Username enter exception: {username}")

    def enterPassword(self,password):
        if self.paths.send_keys_xpath(self.password_field,text=password):
            self.logger.info("Password entered successfully")
        else:
            self.logger.error("Password enter Exception")

    def clickLogin(self):
        if self.paths.click_xpath(self.submit_button):
            self.logger.info("click login success")
        else:
            self.logger.error("Login click exception")

    def error(self):
        error_message = self.paths.get_element_text(self.error_msg)
        return error_message
    
    def success(self):
        success_message = self.paths.get_element_text(self.success_product_tag)
        return success_message

    def login(self,username,password):
        self.enterUsername(username=username)
        self.enterPassword(password=password)
        self.clickLogin()
