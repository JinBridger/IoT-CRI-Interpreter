from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def click_btn(driver, text):
    btn = driver.find_element(By.XPATH, '//button[text()="' + text + '"]')
    btn.click()


def click_span(driver, text):
    span = driver.find_element(By.XPATH, '//span[text()="' + text + '"]')
    span.click()


trigger_device = "test"
trigger_condition = "A new thing was created"
action_device = "test"
action_action = "Create a new thing"

driver = webdriver.Edge()

driver.get("https://ifttt.com/login?wp_=1")

username_elem = driver.find_element(By.NAME, "user[username]")

username_elem.clear()
username_elem.send_keys("928150677@qq.com")

password_elem = driver.find_element(By.NAME, "user[password]")

password_elem.clear()
password_elem.send_keys("zyk220184457")

login_btn = driver.find_element(By.NAME, "commit")
login_btn.click()

driver.get("https://ifttt.com/create")

click_btn(driver, "Add")

time.sleep(2)

click_span(driver, trigger_device)

time.sleep(2)


click_span(driver, trigger_condition)

time.sleep(2)


click_btn(driver, "Add")

time.sleep(2)

click_span(driver, action_device)

time.sleep(2)

click_span(driver, action_action)

time.sleep(2)

click_btn(driver, "Continue")

time.sleep(2)

click_btn(driver, "Finish")

# add_btn = driver.find_element(By.XPATH, '//button[text()="Add"]')
# add_btn.click()


time.sleep(5)

driver.quit()
