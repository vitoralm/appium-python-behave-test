Feature: Tests for BookSearch mobile application

    @wip
    Scenario: Access book details
        Given I am at the launch page and click in the search bar
        When I search for "John" books
        Then I should see a list of books
        And click exaclty the book named "Self-knowledge"
        Then I should see the publisher name "Printed for J. Buckland [etc.]"
        And I should see the book title "Self-knowledge"
        When I click the share icon up-right the screen
        Then I should see the Android default share tray
        When I use the backpress button
        Then I should see the book title "Self-knowledge"
        When I use the backpress button
        Then I should see a list of books