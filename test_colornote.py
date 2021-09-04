import unittest
from setup import Setup as Android
from appium.webdriver.common.touch_action import TouchAction


class Test_ColorNote_4_3_4(unittest.TestCase):
    """ Test ColorNotes 4.3.4 """
    @classmethod
    def setUpClass(cls):
        """ Set webdriver configurations """
        cls.driver = Android.driver
        cls.action = TouchAction(Android.driver)
        cls.page = Android.page

    def setUp(self):
        """ Wait amount of time each unit test """
        self.page.implicitly_wait(3)

    def test_a_Skip_button(self):
        """ Click on startup skip button """
        self.page.skip()

    def test_b_Menu(self):
        """ Click on buttons to adding a new note """
        self.page.menu_adding_note()
        self.page.menu_adding_note_text()

    def test_c_Editing_note(self):
        """ Send keyword to note """

        def file(path):
            with open(path, 'r', newline='') as file:
                """ Open text from a file """
                for line in file.readlines():
                    pass
                file.close()
            return line

        self.page.editing_note_title(
            title='''
            ColorNote 4.3.4
            '''
        )

        self.page.editing_note_text(
            text=file('text.txt')
            # text = 'NOTE TEXTBOX TEST 123456789' * 99999
        )

    @classmethod
    def tearDownClass(cls):
        """ End of test """
        Android.page.back_button(3)
        Android().close_app()


if __name__ == '__main__':
    unittest.main(verbosity=2)
