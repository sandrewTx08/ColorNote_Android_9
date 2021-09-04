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
        self.driver.find_element(*Locators.SKIP).click()
    
    """ Menu """
    def menu_adding_note(self):
        self.driver.find_element(*Locators.ADD_NOTE_BUTTON).click()
        
    def menu_adding_note_text(self):
        self.driver.find_element(*Locators.ADD_TEXT_BUTTON).click()
    
    """ Editing """
    def editing_note_title(self, title):
        self.driver.find_element(*Locators.TYPE_TITLE_TEXT).send_keys(title)

    def editing_note_text(self, text):
        self.driver.find_element(*Locators.TYPE_TEXT).send_keys(text)
