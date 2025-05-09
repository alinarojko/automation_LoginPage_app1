from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base_page import BasePage


class ExceptionsPage(BasePage):
    __url = "https://practicetestautomation.com/practice-test-exceptions/"
    __add_button_locator = (By.ID, "add_btn")
    __row1_input_field = (By.XPATH, "//div[@id='row1']//input[@value='Pizza']")
    __row2_input_element = (By.XPATH, "//div[@id='row2']//input[@class='input-field']")
    __save_button_locator_row1 = (By.XPATH, "//div[@id='row1']//button[@id='save_btn']")
    __save_button_locator_row2 = (By.XPATH, "//div[@id='row2']//button[@id='save_btn']")
    __confirmation_message_locator = (By.XPATH, "//div[@id='confirmation']")
    __edit_button_locator = (By.XPATH, "//button[@id='edit_btn']")
    __instruction_locator = (By.ID, "instructions")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def edit(self):
        super()._click(self.__edit_button_locator)
        super()._clear(self.__row1_input_field)
        super()._type(self.__row1_input_field, "Sushi", time=5)
        super()._click(self.__save_button_locator_row1)

    def add_new_value(self):
        super()._click(self.__add_button_locator)
        super()._type(self.__row2_input_element, "Sushi")
        super()._click(self.__save_button_locator_row2)

    def add_second_row(self):
        super()._click(self.__add_button_locator)
        super()._wait_until_element_is_visible(self.__row2_input_element)

    def is_row2_displayed(self) -> bool:
        return super()._is_displayed(self.__row2_input_element)

    def save_new_value(self):
        super()._click(self.__save_button_locator_row2)

    def save_edit_value(self):
        super()._click(self.__save_button_locator_row1)

    def get_confirmation_message(self) -> str:
        return super()._get_text(self.__confirmation_message_locator, time=5)

    def is_confirmation_message_shown(self) -> bool:
        return super()._is_displayed(self.__confirmation_message_locator)

    def is_instruction_shown(self) -> bool:
        return super()._is_displayed(self.__instruction_locator)

    def clear(self):
        super()._click(self.__edit_button_locator)
        super()._wait_until_element_is_visible(self.__row1_input_field)
        super()._clear(self.__row1_input_field)

    def edit_value(self):
        super()._type(self.__row1_input_field, text="Suuuushiiii")
