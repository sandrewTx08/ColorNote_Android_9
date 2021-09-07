from behave import *
import sys
sys.path.append('../..')
from setup import Setup as Android


@given(u'first app running (1)')
def step_impl(context):
    Android.page.creating_text()
    Android.page.implicitly_wait(3)
    Android.page.creating_checkbox()
    Android.page.implicitly_wait(3)
    Android.page.final_step()

@when(u'"Welcome to ColorNote" show up')
def step_impl(context):
    pass

@then(u'tap on right arrow button')
def step_impl(context):
    pass

@then(u'tap to create note button')
def step_impl(context):
    pass

@then(u'tap add text note type')
def step_impl(context):
    pass

@then(u'type some text')
def step_impl(context):
    pass

@then(u'press tree back button to close keyboard and save')
def step_impl(context):
    pass
@given(u'user continue the tutorial')
def step_impl(context):
    pass

@when(u'"Create a checklist" show up')
def step_impl(context):
    pass

@then(u'tap create a note button')
def step_impl(context):
    pass

@then(u'tap add checklist')
def step_impl(context):
    pass


@then(u'tap at title textbox')
def step_impl(context):
    pass


@then(u'tap "Add item"')
def step_impl(context):
    pass


@then(u'tap "Add item" textbox')
def step_impl(context):
    pass


@then(u'tap "Next"')
def step_impl(context):
    pass


@then(u'tap "OK"')
def step_impl(context):
    pass

@then(u'press twice back button to save')
def step_impl(context):
    pass

@when(u'"Open the saved note" show up')
def step_impl(context):
    pass

@then(u'tap on last added note')
def step_impl(context):
    pass

@then(u'on Pick up laundry')
def step_impl(context):
    pass

@then(u'tap edit the note')
def step_impl(context):
    pass

@then(u'tap on change note color button')
def step_impl(context):
    pass

@then(u'choose color red')
def step_impl(context):
    pass

@then(u'press back button to save')
def step_impl(context):
    pass

@then(u'tap on editing note')
def step_impl(context):
    pass

@then(u'tap pin status bar (dropdown menu)')
def step_impl(context):
    pass

@then(u'tap reminder')
def step_impl(context):
    pass

@then(u'tap "Pin to status bar"')
def step_impl(context):
    pass

@then(u'twice back button to save')
def step_impl(context):
    pass