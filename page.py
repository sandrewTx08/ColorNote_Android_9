from locators import Locators
from time import sleep


class PageObjects(object):
    def __init__(self, driver):
        self.driver = driver

    def implicitly_wait(self, secs):
        """ Wait for elements appear """
        self.driver.implicitly_wait(secs)
        sleep(secs)

    def back_button(self, amount):
        """ Replicate back function from Android """
        for foo in range(amount):
            self.driver.back()

    def skip(self):
        """ Click on startup skip button """
        self.driver.find_element(*Locators.SKIP).click()

    def adding_note(self):
        """ Click on buttons to adding a new note """
        self.driver.find_element(*Locators.ADD_NOTE_BUTTON).click()
        self.driver.find_element(*Locators.ADD_TEXT_BUTTON).click()

    def editing_note(self, title, text):
        """ Send keywords to title and note textbox """
        self.driver.find_element(*Locators.TYPE_TITLE_TEXT).send_keys(title)
        self.driver.find_element(*Locators.TYPE_TEXT).send_keys(text)

