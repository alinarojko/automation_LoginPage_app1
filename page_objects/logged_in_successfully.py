from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from page_objects.base_page import BasePage


class LoggedInSuccessfullyPage(BasePage):
    _url = "https://practicetestautomation.com/logged-in-successfully/"
    __header_locator = (By.TAG_NAME, "h1")
    __log_out_button_locator = (By.LINK_TEXT, "Log out")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def get_expected_url(self) -> str:
        return self._url

    @property
    def get_header(self):
        return super().get_text(self.__header_locator)

    def _is_logout_button_displayed(self, __log_out_button_locator) -> bool:
        return super()._is_displayed(self.__log_out_button_locator)


