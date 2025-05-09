import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from conftest import driver
from page_objects.base_page import BasePage
from page_objects.exceptions_page import ExceptionsPage


class TestException():

    @pytest.mark.exceptions
    def test_no_such_element_exception(self, driver):
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        exceptions_page.add_second_row()
        assert exceptions_page.is_row2_displayed(), "Row 2 Input should be displayed , but it is not"


    @pytest.mark.exceptions
    def test_element_not_interectable_exception(self, driver):
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        exceptions_page.add_new_value()
        assert exceptions_page.is_confirmation_message_shown(), "Row 2 wasn't saved"


    @pytest.mark.exceptions
    def test_invalid_element_sate_exception(self, driver):
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        exceptions_page.clear()
        exceptions_page.edit_value()
        exceptions_page.save_edit_value()
        assert exceptions_page.get_confirmation_message() == "Row 1 was saved", "Confirmation message is not expected"

    @pytest.mark.debug
    @pytest.mark.exceptions
    def test_stale_element_reference_exception(self, driver):
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        exceptions_page.add_second_row()
        assert not exceptions_page.is_instruction_shown(), "Instruction text element should not be displayed"

    @pytest.mark.exceptions
    def test_timeout_exception(self, driver):
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        exceptions_page.add_second_row()
        assert exceptions_page.is_row2_displayed(), 'Row 2 Input should be displayed , but it is not '