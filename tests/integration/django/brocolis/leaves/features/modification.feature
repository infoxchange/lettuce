Feature: Live modification of view code
  Scenario: Modifications do not apply
    Given I change the view code
    Then the root page says "OK"

  Scenario: Modifications apply
    Given I change the view code
    Then the root page says "Changed"
