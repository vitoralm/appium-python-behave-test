Feature: Tests for BookSearch mobile application

    @wip
    Scenario: Access book details
        Given I am at the launch page and click in the search bar
        When I search for "lord of the rings" books
        And click for the first result
        Then I should see the publisher name "Houghton Mifflin Company"
        And I should see the book title "The Lord of the Rings"
        When I use the backpress button
        Then I should see a list of books
        And click exaclty the book named "The Fellowship of the Ring"
        Then I should see the publisher name "Quality Paperback Book Club"
        And I should see the book title "The Fellowship of the Ring"
        When I click the share icon up-right the screen
        Then I should see the Android default share tray
        When I use the backpress button
        Then I should see the book title "The Fellowship of the Ring"
        When I use the backpress button
        Then I should see a list of books
        