import pytest
from conftest import driver
from page_objects.logged_in_successfully import LoggedInSuccessfullyPage
from page_objects.login_page import LoginPage


class TestPositiveScenarious:
    @pytest.mark.login
    @pytest.mark.positive
    def test_positive_login(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login("student", "Password123")
        logged_in_page = LoggedInSuccessfullyPage(driver)
        assert logged_in_page.get_expected_url == logged_in_page.get_current_url , "Actual  URL is not the same as expected "
        assert logged_in_page.get_header == "Logged In Successfully", "Header is not expected "
        assert logged_in_page._is_logout_button_displayed, "Logout button should be displayed"


class TestNegativeScenarious:
    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize("username, password, expected_error_message",
                             [("incorrect_user", "Password123", "Your username is invalid!"),
                              ("student", "Incorrect_password", "Your password is invalid!")])
    def test_negative_login(self, driver, username, password, expected_error_message):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login(username, password)
        assert login_page.get_error_message() == expected_error_message, "The error message is not displayed"



