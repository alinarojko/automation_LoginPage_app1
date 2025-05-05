import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService, Service
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from tests.test_loginpage import ChromeService, driver


class TestNegativeScenarious:
    @pytest.mark.login
    @pytest.mark.negative
    def test_negative_username(self, driver):
        driver = webdriver.Chrome()

        # Go to webpage
        driver.get("https://practicetestautomation.com/practice-test-login/")

        # Type username student into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("incorectuser")

        # Type password Password123 into Password field
        password_locator = driver.find_element(By.XPATH, "//input[@id='password']")
        password_locator.send_keys("Password1234")

        # Push Submit button
        button_locator = driver.find_element(By.ID, "submit")
        button_locator.click()
        time.sleep(2)

        # Verify the error message is displayed
        error_locator = driver.find_element(By.ID, "error")
        assert error_locator.is_displayed(), "Error message is not displayed, but it should"
        error_message = error_locator.text
        assert error_message == "Your username is invalid!", "Error message is not expected"