from BOT.utils.paths import Path_Utils

class Home:

    search_field = "(//span[.='Search'])[last()]"
    search_bar = "//input[@aria-label='Search input']"
    user_btn = "(//span[contains(text(),'divyansh')])[1]" # should not be in stories
    posts_row = "//a[@href='/divyanshhhrathee/']/../../div/div/div/div/div"
    posts = "//a[@href='/divyanshhhrathee/']/../../div/div/div/div/div/div/a"
    images = "//div/img"
    scroll_bottom= "window.scrollTo(0, document.body.scrollHeight);"

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

    def search_user(self,user,num_image=15):

        # Capping max image parameter
        max_images = 50
        num_image = min(max_images,num_image)

        self.log_action(self.paths.click_xpath(self.search_field),
                        "Search Field click success",
                        "Search Field click exception")
        
        self.log_action(self.paths.send_keys_xpath(self.search_bar,text=user),
                        f"Search bar {user} sent successfully",
                        f"Search bar {user} sent exception")
        
        self.log_action(self.paths.click_xpath(f"(//span[contains(text(),'{user[0:5]}')])[1]"),
                        "User profile click success",
                        "User profile click exception")

        for x in range(num_image):
            if x in [11,23,35,47,59]:
                self.driver.execute_script(self.scroll_bottom)
            element = self.paths.get_element(f"(//a/div/div/img)[{x+1}]")
            try:
                self.paths.append_screenshot(user,element=element)
                print(f"{x+1} image captured done...")
                self.logger.info(f"{x+1} image captured done...")
            except Exception as e:
                self.logger.error(f"Could not append due to {str(e)}")
                print(f"Could not append due to {str(e)}")
        

        