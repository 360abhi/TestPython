import os
import sys
from pathlib import Path

root_path = Path(__file__).parent.parent.parent
sys.path.append(str(root_path))

from BOT.Driver.driver import setup_webdriver
from BOT.Classes.Home import Home
from BOT.Classes.Login import Login

driver = setup_webdriver()
driver.get('https://www.instagram.com/')
home = Home(driver=driver)
login = Login(driver=driver)

login.login(username='123',password='123')
home.search_user('demouser',num_image=15)

driver.quit()