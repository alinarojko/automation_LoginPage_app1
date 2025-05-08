import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from conftest import driver


class TestException:

    @pytest.mark.exceptions
    def test_no_such_element_exception(self, driver):
        # Open the page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Click Add button
        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()

        # Explicit wait , can be used to find element and wait for it appearance
        wait = WebDriverWait(driver, 10)
        row2_input_element = wait.until(ec.presence_of_element_located((By.XPATH,
                                        "//div[@id='row2']//input[@class='input-field']")))

        # Verify Row 2 input field is displayed
        assert row2_input_element.is_displayed(), 'Row 2 Input should be displayed , but it is not '

    @pytest.mark.exception
    def test_element_not_interectable_exception(self, driver):
        # Open the page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Click Add button
        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()

        # Explicit wait , can be used to find element and wait for it appearance
        wait = WebDriverWait(driver, 5)
        row2_input_element = wait.until(ec.presence_of_element_located((By.XPATH,
                                        "//div[@id='row2']//input[@class='input-field']")))

        # Verify Row 2 input field is displayed
        assert row2_input_element.is_displayed(), 'Row 2 Input should be displayed , but it is not '

        # Type text into the second input field
        row2_input_element.send_keys("New element - soup")

        # Push Save button
        save_button_locator = driver.find_element(By.XPATH, "//div[@id='row2']//button[@id='save_btn']")
        save_button_locator.click()

        # Verify text was saved
        confirmation_message_locator = wait.until(ec.visibility_of_element_located((By.XPATH,
                                                                                    "//div[@id='confirmation']")))
        message = confirmation_message_locator.text
        assert message == "Row 2 was saved", "Message is not expected"

    @pytest.mark.exception
    def test_invalid_element_sate_exception(self, driver):
        # Open the page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Clear input field
        edit_button_locator = driver.find_element(By.XPATH, "//button[@id='edit_btn']")
        edit_button_locator.click()
        row1_input_field = driver.find_element(By.XPATH, "//div[@id='row1']//input[@value='Pizza']")
        wait = WebDriverWait(driver, 10)
        wait.until(ec.element_to_be_clickable(row1_input_field))
        row1_input_field.clear()

        # Type text to the input field
        row1_input_field.send_keys("Sushi")

        # Push Save button
        save_button_locator = driver.find_element(By.XPATH, "//div[@id='row1']//button[@id='save_btn']")
        save_button_locator.click()

        # Verify text Changed
        confirmation_message_locator = wait.until(ec.visibility_of_element_located((By.XPATH,
                                                                                    "//div[@id='confirmation']")))
        message = confirmation_message_locator.text
        assert message == "Row 1 was saved", "Message is not expected"

    @pytest.mark.exception
    def test_stale_element_reference_exception(self, driver):

        # Open the page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Push add button
        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()

        # Verify instruction text element is no longer displayed
        wait = WebDriverWait(driver, 10)
        assert wait.until(ec.invisibility_of_element_located((By.ID, "instructions")), "Instruction text element should not be displayed")

    @pytest.mark.debug
    @pytest.mark.exception
    def test_timeout_exception(self, driver):
        # Open the page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Push add button
        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()

        # Wait for 3 seconds input field to be displayed
        wait = WebDriverWait(driver, 5)
        row2_input_element = wait.until(ec.visibility_of_element_located((By.XPATH,
                                        "//div[@id='row2']//input[@class='input-field']")),
                                        "Failed waiting for the row2_input to be visible")

        # Verify second input field is displayed
        assert row2_input_element.is_displayed(), 'Row 2 Input should be displayed , but it is not '
