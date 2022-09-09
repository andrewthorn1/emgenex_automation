from base.seleniumbase import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement
from typing import List
from base.utils import Utils
from selenium.webdriver.common.keys import Keys
import time



class HomepageNav(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__nav_links: str = '.headermenuList>li'
        self.__first_big_banner_locator: str = '//img[@alt="BannerRightBg2"]'
        self.NAV_LINK_TEXT = 'Home,Solutions,About Us,Contact Us'

    def get_nav_links(self) -> List[WebElement]:
        return self.are_visible('css', self.__nav_links, 'Header Navigation Links')

    def get_nav_links_text(self) -> str:
        nav_links = self.get_nav_links()
        nav_links_text = self.get_text_from_webelements(nav_links)
        return Utils.join_strings(nav_links_text)

    def get_first_big_right_banner(self) -> WebElement:
        return self.is_visible('xpath', self.__first_big_banner_locator, 'First big right banner')
