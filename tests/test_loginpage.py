import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService, Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def driver():
    print("Creating Chrome Driver")
    my_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield my_driver
    my_driver.quit()
    print("Closing Chrome Driver")


class ChromeService:
    pass


class TestPositiveScenarious:
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


