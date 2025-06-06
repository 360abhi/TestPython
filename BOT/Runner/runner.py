import os
from dotenv import load_dotenv
import sys
from pathlib import Path
root_path = Path(__file__).parent.parent.parent
sys.path.append(str(root_path))
from BOT.Driver.driver import setup_webdriver
from BOT.Classes.Home import Home
from BOT.Classes.Login import Login
from BOT.Logging.logger import setup_logger

def execute():

    try:
        load_dotenv(override=True)
        username = os.getenv('USERNAME')
        password = os.getenv('PASSWORD')
        user = os.getenv('USER')

        logger = setup_logger(user)
        driver = setup_webdriver()
        driver.get('https://www.instagram.com/')
        home = Home(driver=driver,logger=logger)
        login = Login(driver=driver,logger=logger)

        login.login(username=username,password=password)
        home.search_user(user=user,num_image=12)

    except Exception as e:
        print(str(e))

    finally:
        driver.quit()

if __name__ == "__main__":
    execute()