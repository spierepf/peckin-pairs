@admin
Feature: Logging in as the superuser

  Scenario: Logging in as the superuser
    When a user logs in as the superuser
    Then the user will see the admin page
