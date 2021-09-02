from appium import webdriver
from page import PageObjects


class Setup(object):
    driver = webdriver.Remote('http://localhost:4723/wd/hub', {
        "platformName": "Android",
        "deviceName": "0062311931",
        "app": r"D:\\mobile\\color_note_4_3_4.apk",
        "autoGrantPermissions": "true",
        "platformVersion": "9",
        # "noReset": "true",
        # "fullReset": "false",
        # "dontStopAppOnReset": "true"
    })

    def close_app(self):
        self.driver.quit()

    page = PageObjects(driver)