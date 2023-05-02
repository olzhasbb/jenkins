from argparse import Action
import pytest
import time
import pytest
#@pytest.mark.fast

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
def test_google_search(browser):
    browser.get('https://google.com')
    search_box = browser.find_element(By.NAME, 'q')

#driver = None

#def setup_module(module):
#    global driver
 ##  driver.implicitly_wait(10)
   # driver.delete_all_cookies()
    #driver.get('https://aliexpress.com')


#def teardown_module(module):
    #driver.quit()


#def test_google_title():
    #assert driver.title == "Aliiii"


#def test_google_url():
    #assert driver.url == "https://www.aliexpress.us/?gatewayAdapt=glo2usa&_randl_shipto=US"