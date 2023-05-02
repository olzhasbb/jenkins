from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

        self.username_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@name="username"'))
        )

        self.password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@name="password"'))
        )

        self.login_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAMENAME, "_ab8w  _ab94 _ab99 _ab9f _ab9m _ab9p _abcm"))
        )

    def enter_username(self, email):
        self.username_input.clear()
        self.username_input.send_keys("username")

    def enter_password(self, password):
        self.password_input.clear()
        self.password_input.send_keys("password")

    def click_login_button(self):
        self.login_button.click()

def test_login():
    driver = webdriver.Chrome()
    driver.get("https://www.instagram.com/")
    login_page = LoginPage(driver)
    login_page.enter_username("username")
    login_page.enter_password("password")
    login_page.click_login_button()
    assert driver.current_url != "http://www.example.com/dashboard"
    assert driver.title != "Login"
    driver.quit()

