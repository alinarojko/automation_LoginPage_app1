import pytest
from selenium.webdriver.common.by import By
from conftest import driver
import time


class TestPositiveScenarious:
    # Open page
    # Type username student into Username field
    # Type password Password123 into Password field
    # Push Submit button
    # Verify new page URL contains practicetestautomation.com/logged-in-successfully/
    # Verify new page contains expected text ('Congratulations' or 'successfully logged in')
    # Verify button Log out is displayed on the new page

    @pytest.mark.login
    @pytest.mark.positive
    def test_positive_login(self, driver):
        # Go to webpage
        driver.get("https://practicetestautomation.com/practice-test-login/")
        time.sleep(3)

        # Type username student into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("student")

        # Type password Password123 into Password field
        password_locator = driver.find_element(By.XPATH, "//input[@id='password']")
        password_locator.send_keys("Password123")

        # Push Submit button
        button_locator = driver.find_element(By.ID, "submit")
        button_locator.click()
        time.sleep(3)

        # Verify new page URL contains practicetestautomation.com/logged-in-successfully/
        actual_url = driver.current_url
        assert actual_url == "https://practicetestautomation.com/logged-in-successfully/"

        # Verify new page contains expected text ('Congratulations' or 'successfully logged in')
        congratulation_locator = driver.find_element(By.TAG_NAME, "h1")
        text = congratulation_locator.text
        assert text == "Logged In Successfully"

        # Verify button Log out is displayed on the new page
        logout_locator = driver.find_element(By.LINK_TEXT, "Log out")
        assert logout_locator.is_displayed()


class TestNegativeScenarious:
    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize("username, password, expected_error_message",
                             [("incorrect_user", "Password123", "Your username is invalid!"),
                              ("student", "Incorrect_password", "Your password is invalid!")])
    def test_negative_login(self, driver, username, password, expected_error_message):
        # Go to webpage
        driver.get("https://practicetestautomation.com/practice-test-login/")

        # Type username student into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys(username)

        # Type password Password123 into Password field
        password_locator = driver.find_element(By.XPATH, "//input[@id='password']")
        password_locator.send_keys(password)

        # Push Submit button
        button_locator = driver.find_element(By.ID, "submit")
        button_locator.click()
        time.sleep(2)

        # Verify the error message is displayed
        error_locator = driver.find_element(By.ID, "error")
        assert error_locator.is_displayed(), "Error message is not displayed, but it should"
        error_message = error_locator.text
        assert error_message == expected_error_message, "Error message is not expected"
