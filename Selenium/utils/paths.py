from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec

class Path_Utils:

    def __init__(self,driver,timeout=10):
        self.driver = driver
        self.timeout = timeout

    def click_xpath(self,xpath):
        try:
            element = WebDriverWait(self.driver,timeout=self.timeout).until(
                Ec.element_to_be_clickable((By.XPATH,xpath))
            )
            element.click()
            return True
        except Exception as e:
            print(str(e))
            print(f"Exception durint xpath of {xpath}")
            return False

    def send_keys_xpath(self,xpath,text:str):
        try:
            element = WebDriverWait(self.driver,timeout=self.timeout).until(
                Ec.visibility_of_element_located((By.XPATH,xpath))
            )
            element.send_keys(text)
            return True
        except Exception as e:
            print(str(e))
            print(f"Exception during xpath {xpath}")
            return False

    def clear_xpath(self,xpath):
        try:
            element = WebDriverWait(self.driver,timeout=self.timeout).until(
                Ec.element_to_be_clickable((By.XPATH,xpath))
            )
            element.clear()
            return True
        except Exception as e:
            print(str(e))
            print(f"Exception during xpath {xpath}")
            return False
        
    def get_element(self,xpath):
        try:
            element = WebDriverWait(self.driver,timeout=self.timeout).until(
                Ec.visibility_of_element_located((By.XPATH,xpath))
            )
            return element
        except Exception as e:
            print(str(e))

    def get_element_text(self,xpath):
        try:
            element = WebDriverWait(self.driver,timeout=self.timeout).until(
                Ec.visibility_of_element_located((By.XPATH,xpath))
            )
            return str(element.text)
        except Exception as e:
            print(str(e))
            return "NO ELEMENT FOUND"
