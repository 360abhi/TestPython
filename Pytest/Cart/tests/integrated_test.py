import pytest
import os
from pathlib import Path
from selenium.webdriver.common.alert import Alert
import sys
root_path = Path(__file__).parent.parent.parent.parent
sys.path.append(str(root_path))
import time
from Pytest.Project.driver import setup_webdriver
from Pytest.Cart.Pages.Home import Home_Page
from Pytest.Cart.Pages.Login import Login_Page
from BOT.Logging.logger import setup_logger

@pytest.fixture
def driver():
    webdriver = setup_webdriver()
    webdriver.get('https://www.saucedemo.com/v1/')
    yield webdriver
    webdriver.quit()

@pytest.fixture
def logger():
    log = setup_logger('sauce_demot')
    return log


@pytest.fixture
def login(driver,logger):
    setup_login = Login_Page(driver,logger)
    return setup_login

@pytest.fixture
def home(driver,logger):
    setup_home = Home_Page(driver,logger)
    return setup_home

@pytest.mark.parametrize("username,password,items,firstname,lastname,zip",[
    ("standard_user","secret_sauce",['Sauce Labs Bolt T-Shirt','Sauce Labs Bike Light'],"abhishek","chhawari","123401")
])
def test_flow(login,home,username,password,items,firstname,lastname,zip):
    login.enter_username(username)
    login.enter_password(password)
    login.click_login()
    time.sleep(555)
    home.add_to_cart(items)
    cart_count = home.get_cart_count()
    assert cart_count == str(2)
    home.go_to_cart()
    home.checkout()
    home.add_details(firstname,lastname,zip)
    price = home.get_total_item_price()
    print(price)
    home.click_finish()
    message = home.get_thankyou_text()
    print(message)

