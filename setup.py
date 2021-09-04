import os
from appium import webdriver
from page import PageObjects


class Setup(object):
    capability = {
        "platformName": "Android",
        "deviceName": "0062311931",
        "autoGrantPermissions": "true",
        "app": f"{os.getcwd()}\\app\\color_note_4_3_4.apk",
        "platformVersion": "9",
        # "noReset": "true",
        # "fullReset": "false",
        # "dontStopAppOnReset": "true"
    }
    driver = webdriver.Remote('http://localhost:4723/wd/hub', capability)
    page = PageObjects(driver)

    def close_app(self):
        self.driver.quit()
