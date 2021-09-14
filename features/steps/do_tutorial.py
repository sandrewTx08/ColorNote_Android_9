import random
import string
from behave import *
import sys
sys.path.append('../..')
from setup import Setup as Android


@given(u'first app running (1)')
def step_impl(context):
    Android.page.press_start_tutorial()

@when(u'"Welcome to ColorNote" show up')
def step_impl(context):
    pass

@then(u'tap on right arrow button')
def step_impl(context):
    Android.page.press_skip(1)

@then(u'tap to create note button')
def step_impl(context):
    Android.page.press_skip(1)

@then(u'tap add text note type')
def step_impl(context):
    pass

@then(u'type some text')
def step_impl(context):
    Android.page.editing_note_title('Hello World')
    Android.page.editing_note_text(''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(9999)))

@then(u'press tree back button to close keyboard and save')
def step_impl(context):
    Android.page.back_button(3)

@given(u'user continue the tutorial (1)')
def step_impl(context):
    Android.page.press_start_tutorial()

@when(u'"Create a checklist" show up')
def step_impl(context):
    Android.page.press_skip(1)

@then(u'tap create a note button')
def step_impl(context):
    Android.page.press_skip(1)

@then(u'tap add checklist')
def step_impl(context):
    Android.page.press_skip(1)

@then(u'tap at title textbox')
def step_impl(context):
    Android.page.press_skip(1)

@then(u'tap "Add item"')
def step_impl(context):
    Android.page.press_skip(1)

@then(u'tap "Add item" textbox')
def step_impl(context):
    Android.page.press_skip(1)

@then(u'tap "Next"')
def step_impl(context):
    Android.page.press_skip(1)

@then(u'tap "OK"')
def step_impl(context):
    Android.page.press_skip(1)

@then(u'press twice back button to save')
def step_impl(context):
    Android.page.back_button(1)

@given(u'user continue the tutorial (2)')
def step_impl(context):
    Android.page.press_skip(1)

@when(u'"Open the saved note" show up')
def step_impl(context):
    Android.page.press_start_tutorial()

@then(u'tap on last added note')
def step_impl(context):
    Android.page.press_skip(1)

@then(u'on Pick up laundry')
def step_impl(context):
    Android.page.press_skip(1)

@then(u'tap edit the note')
def step_impl(context):
    Android.page.press_skip(1)

@then(u'tap on change note color button')
def step_impl(context):
    Android.page.press_skip(1)

@then(u'choose color red')
def step_impl(context):
    Android.page.press_skip(1)

@then(u'press back button to save')
def step_impl(context):
    Android.page.back_button(2)

@then(u'tap on editing note')
def step_impl(context):
    Android.page.press_skip(1)

@then(u'tap pin status bar (dropdown menu)')
def step_impl(context):
    Android.page.press_skip(1)

@then(u'tap reminder')
def step_impl(context):
    Android.page.press_skip(1)

@then(u'tap "Pin to status bar"')
def step_impl(context):
    Android.page.press_skip(1)

@then(u'twice back button to save')
def step_impl(context):
    Android.page.back_button(2)