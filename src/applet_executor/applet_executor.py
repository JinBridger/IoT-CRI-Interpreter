from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import time
import sys
from sqlite_interface import SqliteInterface


class AppletExecutor:
    keys_path = "../../keys/keys.json"

    def __init__(self, infos: dict) -> None:
        self.trigger_device = infos["trigger_device"]
        self.trigger_condition = infos["trigger_condition"]
        self.action_device = infos["action_device"]
        self.action_action = infos["action_action"]
        self.is_pro = infos["is_pro"]
        self.priority = infos["priority"]

        with open(self.keys_path, "r") as f:
            keys = json.load(f)
        self.email = keys["email"]
        self.password = keys["password"]

        self.sql = SqliteInterface()
        self.sql.add_applet(
            self.trigger_device,
            self.trigger_condition,
            self.action_device,
            self.action_action,
            self.is_pro,
            self.priority,
        )

        self.driver = webdriver.Edge()

    def login(self):
        self.driver.get("https://ifttt.com/login?wp_=1")

        username_elem = self.driver.find_element(By.NAME, "user[username]")
        username_elem.clear()
        username_elem.send_keys("928150677@qq.com")

        password_elem = self.driver.find_element(By.NAME, "user[password]")
        password_elem.clear()
        password_elem.send_keys("zyk220184457")

        login_btn = self.driver.find_element(By.NAME, "commit")
        login_btn.click()

    def click_btn(self, text):
        btn = self.driver.find_element(By.XPATH, '//button[text()="' + text + '"]')
        btn.click()
        time.sleep(2)

    def click_span(self, text):
        span = self.driver.find_element(By.XPATH, '//span[text()="' + text + '"]')
        span.click()
        time.sleep(2)

    def execute(self):
        self.driver.get("https://ifttt.com/create")

        self.click_btn("Add")
        self.click_span(self.trigger_device)
        self.click_span(self.trigger_condition)

        self.click_btn("Add")
        self.click_span(self.action_device)
        self.click_span(self.action_action)

        self.click_btn("Continue")
        self.click_btn("Finish")

        self.driver.quit()


if __name__ == "__main__":
    ad = {
        "trigger_device": sys.argv[1],
        "trigger_condition": sys.argv[2],
        "action_device": sys.argv[3],
        "action_action": sys.argv[4],
        "is_pro": sys.argv[5],
        "priority": sys.argv[6],
    }
    ae = AppletExecutor(ad)
    ae.login()
    ae.execute()
