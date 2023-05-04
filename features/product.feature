    Feature: checkout products

    Scenario: checkout a product
        Given we submit a product
        When we fill in the form
        Then it succeeds