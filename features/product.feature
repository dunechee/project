    Feature: search products

    Scenario: checkout a product
        Given we search a product
        When we enter the query
        Then it succeeds