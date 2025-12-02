#coding=uft-8
Feature: Login
    Scenario: open website
        When I open the login website
        Then I input username
        Then I input password