Feature: Do tutorial
  User perform the tutorial

  Scenario: Creating text
    Given first app running (1)
    When "Welcome to ColorNote" show up
    Then tap on right arrow button
    And tap to create note button
    And tap add text note type
    And type some text
    And press tree back button to close keyboard and save

  Scenario: Creating checkbox
    Given user continue the tutorial (1)
    When "Create a checklist" show up
    Then tap create a note button
    And tap add checklist
    And tap at title textbox
    And tap "Add item"
    And tap "Add item" textbox
    And tap "Next"
    And tap "Add item" textbox
    And tap "OK"
    And press twice back button to save

  Scenario: Final step
    Given user continue the tutorial (2)
    When "Open the saved note" show up
    Then tap on last added note
    And on Pick up laundry
    And tap edit the note
    And tap on change note color button
    And choose color red
    And press back button to save
    And tap on editing note
    And tap pin status bar (dropdown menu)
    And tap reminder
    And tap "Pin to status bar"
    And twice back button to save

