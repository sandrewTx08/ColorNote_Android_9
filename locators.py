from appium.webdriver.common.mobileby import By
# from appium.webdriver.common.mobileby import MobileBy


class Locators(object):
    APP_NAME = 'com.socialnmobile.dictapps.notepad.color.note'

    """ Main menu """
    SKIP = (By.ID, f'{APP_NAME}:id/btn_start_skip')
    ADD_NOTE_BUTTON = (By.ID,  f'{APP_NAME}:id/bottom_fab')
    ADD_TEXT_BUTTON = (By.ID, f'{APP_NAME}:id/icon')

    """ Inside note """
    TYPE_TITLE_TEXT = (By.ID,  f'{APP_NAME}:id/edit_title')
    TYPE_TEXT = (By.ID,  f'{APP_NAME}:id/edit_note')
