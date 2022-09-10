from base.seleniumbase import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement
from typing import List
from selenium.webdriver.common.keys import Keys


class GetInTouchNav(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__first_name_locator: str = 'firstname'
        self.__last_name_locator: str = 'lastname'
        self.__email_locator: str = 'email'
        self.__submit_button_locator: str = 'input[value="Submit"]'
        self.__submitted_message_locator: str = '.submitted-message'
        self.__error_message_locator: str = 'div[class="hs_error_rollup"]'
        self.__radio_button_no_locator: str = '//span[@data-reactid=".hbspt-forms-0.1:$7.$are_you_a_current_customer_.' \
                                              '0.$No.0.1"]'


    def get_first_name_field(self) -> WebElement:
        return self.is_visible("name", self.__first_name_locator)

    def get_last_name_field(self) -> WebElement:
        return self.is_visible("name", self.__last_name_locator)

    def get_email_field(self) -> WebElement:
        return self.is_visible("name", self.__email_locator)

    def get_radio_button_no(self) -> WebElement:
        return self.is_visible("xpath", self.__radio_button_no_locator)

    def get_submit_button(self) -> WebElement:
        return self.is_visible("css", self.__submit_button_locator)

    def get_error_message_text(self) -> str:
        return self.get_text_from_webelement("css", self.__error_message_locator)

    def get_submitted_message_text(self) -> str:
        return self.get_text_from_webelement("css", self.__submitted_message_locator)
