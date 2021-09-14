from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from time import sleep


class PageObjects(object):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

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
        self.wait.until(EC.visibility_of_element_located((Locators.TYPE_TITLE_TEXT))).send_keys(title)

    def editing_note_text(self, text):
        self.wait.until(EC.visibility_of_element_located((Locators.TYPE_TEXT))).send_keys(text)

    """ Do tutorial """
    def press_skip(self, amount):
        for foo in range(amount):
            self.wait.until(EC.visibility_of_element_located((Locators.SKIP_TUTORIAL_BUTTON))).click()

    def press_start_tutorial(self):
        self.wait.until(EC.visibility_of_element_located((Locators.START_TUTORIAL_BUTTON))).click()

    def creating_text(self):
        self.wait.until(EC.visibility_of_element_located((Locators.START_TUTORIAL_BUTTON))).click()
        self.press_skip(2)
        self.wait.until(EC.visibility_of_element_located((Locators.TYPE_TEXT))).send_keys("Do tutorial test")
        self.back_button(3)

    def creating_checkbox(self):
        self.driver.find_element(*Locators.START_TUTORIAL_BUTTON).click()
        self.press_skip(10)
        self.driver.find_element(*Locators.START_TUTORIAL_BUTTON).click()

    def final_step(self):
        self.driver.find_element(*Locators.START_TUTORIAL_BUTTON).click()
        self.press_skip(10)
        self.driver.find_element(*Locators.START_TUTORIAL_BUTTON).click()