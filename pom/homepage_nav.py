from base.seleniumbase import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement
from typing import List
from base.utils import Utils
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time


class HomepageNav(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__nav_links: str = '.headermenuList>li'
        self.__contact_us_link_locator: str = '//a[contains(text(),"Contact Us")]'
        self.__first_big_banner_locator: str = '//img[@alt="BannerRightBg2"]'
        self.__long_term_care_section_locator: str = '//div[@class="EwThreeCol w33 mw100 ib vt"][2]'
        self.__button_learn_more_in_long_term_care_section_locator: str = '//div[@class="EwThreeColInner"]//a[@href=' \
                                                                          '"https://www.emgenex.com/long-term-care"]'
        self.NAV_LINK_TEXT = 'Home,Solutions,About Us,Contact Us'
        self.__first_name_locator: str = 'firstname'
        self.__last_name_locator: str = 'lastname'
        self.__email_locator: str = 'email'
        self.__submit_button_locator: str = 'input[value="Submit"]'
        self.__submitted_message_locator: str = '.submitted-message'
        self.__error_message_locator: str = 'div[class="hs_error_rollup"]'

    def get_nav_links(self) -> List[WebElement]:
        return self.are_visible('css', self.__nav_links, 'Header Navigation Links')

    def get_nav_links_text(self) -> str:
        nav_links = self.get_nav_links()
        nav_links_text = self.get_text_from_webelements(nav_links)
        return Utils.join_strings(nav_links_text)

    def get_first_big_right_banner(self) -> WebElement:
        return self.is_visible('xpath', self.__first_big_banner_locator, 'First big right banner')

    def hover_on_long_term_care_section(self) -> WebElement:
        hover_element = self.is_visible('xpath', self.__long_term_care_section_locator)
        return ActionChains(self.driver).move_to_element(hover_element).perform()

    def get_button_learn_more_in_long_term_care_section(self) -> WebElement:
        return self.is_present('xpath', self.__button_learn_more_in_long_term_care_section_locator, 'Button learn more'
                                                                                                    ' in long term care'
                                                                                                    ' section')

    def get_contact_us_link(self) -> WebElement:
        return self.is_visible('xpath', self.__contact_us_link_locator)

    def get_first_name_field(self) -> WebElement:
        return self.is_visible("name", self.__first_name_locator)

    def get_last_name_field(self) -> WebElement:
        return self.is_visible("name", self.__last_name_locator)

    def get_email_field(self) -> WebElement:
        return self.is_visible("name", self.__email_locator)

    def get_submit_button(self) -> WebElement:
        return self.is_visible("css", self.__submit_button_locator)

    def get_submitted_message_text(self) -> str:
        return self.get_text_from_webelement("css", self.__submitted_message_locator)

    def get_error_message_text(self) -> str:
        return self.get_text_from_webelement("css", self.__error_message_locator)
