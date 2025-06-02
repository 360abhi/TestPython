from BOT.utils.paths import Path_Utils
import time


class Home:

    search_field = "(//span[.='Search'])[last()]"
    search_bar = "//input[@aria-label='Search input']"
    user_btn = "(//span[contains(text(),'divyansh')])[1]" # should not be in stories
    posts_row = "//a[@href='/divyanshhhrathee/']/../../div/div/div/div/div"
    posts = "//a[@href='/divyanshhhrathee/']/../../div/div/div/div/div/div/a"
    images = "//div/img"


    
    def __init__(self,driver):
        self.driver = driver
        self.paths = Path_Utils(self.driver)

    def search_user(self,user,num_image=5):
        time.sleep(3)
        self.paths.click_xpath(self.search_field)
        # time.sleep(2)
        self.paths.send_keys_xpath(self.search_bar,text=user)
        # time.sleep(2)
        self.paths.click_xpath(f"(//span[contains(text(),'{user[0:6]}')])[1]")
        time.sleep(2)
        for x in range(num_image):
            if x in [11,23,35]:
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(5)
            element = self.paths.get_element(f"(//a/div/div/img)[{x+1}]")
            try:
                self.paths.append_screenshot(user,element=element)
                print(f"{x+1} done...")
            except Exception as e:
                print(f"Could not append due to {str(e)}")
            time.sleep(0.5)
        

        