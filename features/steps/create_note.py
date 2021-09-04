from behave import *
import sys
sys.path.append('../..') 
from setup import Setup as Android


class Creating_note:
    @given(u'first app running')
    def step_impl(context):
        pass

    @when(u'skip button show up')
    def step_impl(context):
        Android.page.implicitly_wait(3)

    @then(u'tap skip')
    def step_impl(context):
        Android.page.skip()

    @given(u'the user is at "Note" menu')
    def step_impl(context):
        pass

    @when(u'Notes menu show up')
    def step_impl(context):
        Android.page.implicitly_wait(3)

    @then(u'tap "Add note"')
    def step_impl(context):
        Android.page.menu_adding_note()

    @then(u'tap "Add text"')
    def step_impl(context):
        Android.page.menu_adding_note_text()

    @given(u'user is at "Editing" note menu')
    def step_impl(context):
        pass

    @when(u'user keyboard show up')
    def step_impl(context):
        Android.page.implicitly_wait(3)

    @then(u'type note title')
    def step_impl(context):
        Android.page.editing_note_title(
            title = '''
            ColorNote 4.3.4
            '''
        )

    @then(u'add some text')
    def step_impl(context):
        def file(path):
            with open(path, 'r', newline='') as file:
                """ Open text from a file """
                for line in file.readlines():
                    pass
                file.close()
            return line
           
        Android.page.editing_note_text(
            file('text.txt')
            )
    
        """ End of test """
        Android.page.back_button(3)
