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
        self.__first_big_banner_locator: str = '//img[@alt="BannerRightBg2"]'
        self.__long_term_care_section_locator: str = '//div[@class="EwThreeCol w33 mw100 ib vt"][2]'
        self.__button_learn_more_in_long_term_care_section_locator: str = '//div[@class="EwThreeColInner"]//a[@href=' \
                                                                          '"https://www.emgenex.com/long-term-care"]'
        self.NAV_LINK_TEXT = 'Home,Solutions,About Us,Contact Us'

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
