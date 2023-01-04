Feature: Login
    Scenario:open website
        When I open the login website "http://testdao.site/login"
        Then I input username "admin" and password "admin123"
