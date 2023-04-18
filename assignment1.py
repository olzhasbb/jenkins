from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
import time
driver = webdriver.Chrome()

# navigate to the Google website
driver.get("https://demo.automationtesting.in/Alerts.html")
driver.implicitly_wait(10)
click1 = driver.find_element(By.CSS_SELECTOR, "button[onclick='alertbox()']").click()
time.sleep(2)
alt = driver.switch_to.alert
alt.accept()
time.sleep(2)
click2 = driver.find_element(By.XPATH, '//*[@href = "#CancelTab"]').click()
time.sleep(2)
click3 = driver.find_element(By.CSS_SELECTOR, "button[onclick='confirmbox()']").click()
alt = driver.switch_to.alert
alt.accept()
time.sleep(2)
click4 = driver.find_element(By.XPATH, '//*[@href = "#Textbox"]').click()
time.sleep(2)
click5 = driver.find_element(By.CSS_SELECTOR, "button[onclick='promptbox()']").click()
alt = driver.switch_to.alert
alt.accept()
time.sleep(2)

actions = ActionChains(driver)
actions.click(click1)
actions.click(click2)
actions.click(click3)
actions.click(click4)
actions.click(click5)
actions.perform()
time.sleep(3)