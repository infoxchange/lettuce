Feature: Create users
    Scenario: Can create Django users
        Given I have users in the database:
            | username | password |
            | john     | secret   |
            | paul     | secret   |
        Then there should be 2 users in the database
