Feature: Flask is secure in that users must log in and log out to access certain features

  Scenario: User can log in
    Given we have flask running
    When we log in with "admin" and "admin"
    Then we should see the alert "You were logged in"

  Scenario: Incorrect username
    Given we have flask running
    When we log in with "notadmin" and "admin"
    Then we should see the alert "Invalid username"

  Scenario: Incorrect password
    Given we have flask running
    When we log in with "admin" and "notadmin"
    Then we should see the alert "Invalid password"

  Scenario: User can log out
    Given we have flask running
    And we log in with "admin" and "admin"
    When we logout
    Then we should see the alert "You were logged out"

  Scenario: Successful post
    Given we have flask running
    And we log in with "admin" and "admin"
    When we add a new entry with "test" and "test" as the title and text
    Then we should see the alert "New entry was successfully posted"

  Scenario: Unsuccessful post
    Given we have flask running
    And we are not logged in
    When we add a new entry with "test" and "test" as the title and text
    Then we should see a "401" status code

  Scenario: Show entries
    Given we have flask running
    And we log in with "admin" and "admin"
    When we add a new entry with "test" and "test21" as the title and text
    Then we should see the alert "New entry was successfully posted"
    And we should see the post with "test" and "test21" in title and text