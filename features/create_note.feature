Feature: Creating a note 
    User create note with title and a notation text
    
    Scenario: Opening app 
    Given first app running
    When skip button show up
    Then tap skip
    
    Scenario: Adding a text note
    Given the user is at "Note" menu
    When Notes menu show up
    Then tap "Add note"
    And tap "Add text"

    Scenario: Editing note
    Given user is at "Editing" note menu
    When user keyboard show up
    Then type note title 
    And add some text 
