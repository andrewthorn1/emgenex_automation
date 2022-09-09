from selenium.webdriver.support.wait import WebDriverWait

from base.seleniumbase import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement
from typing import List
from selenium.webdriver.common.keys import Keys


class LongTermCareNav(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__title_locator: str = '//div[@class="font26 fontGre wow fadeInDown"]'

    def get_title_text(self) -> str:
        return self.get_text_from_webelement("xpath", self.__title_locator)
