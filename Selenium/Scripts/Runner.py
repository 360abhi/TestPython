import os
import sys

curr_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(curr_dir,'..','..'))
sys.path.append(root_dir)

from Selenium.Scripts.Login import Login
from Selenium.Data import read as utils
from Selenium.utils.ReadData import Read
from Selenium.Logging.logger import setup_logger
from Selenium.Driver.driver import setup_webdriver



def execute(sheet_name):

    driver = setup_webdriver()

    try:

        data = utils.getData(filepath=Read.INPUT_DATA,sheetname=sheet_name)
        username = str(data['deal_user'].iloc[0])
        password = str(data['deal_password'].iloc[0])
        case = str(data['case'].iloc[0])

        logger = setup_logger(log_name=username)
        driver.get("https://www.saucedemo.com/v1/index.html")

        login = Login(driver=driver,logger=logger)
        login.login(username=username,password=password)
        if case == "negative":
            error = login.error()
            return error
        else:
            success = login.success()
            return success

    except Exception as e:
        print(str(e))

    finally:
        driver.quit()