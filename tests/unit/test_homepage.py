import time

import pytest
from pom.homepage_nav import HomepageNav
from pom.longtermcare_nav import LongTermCareNav


@pytest.mark.usefixtures('setup')
class TestHomepage:

    def test_nav_links(self):
        homepage_nav = HomepageNav(self.driver)
        actual_links = homepage_nav.get_nav_links_text()
        expected_links = homepage_nav.NAV_LINK_TEXT
        assert expected_links == actual_links, 'Validating Header Nav Links Text'

    def test_first_big_right_banner_is_visible(self):
        homepage_nav = HomepageNav(self.driver)
        assert homepage_nav.get_first_big_right_banner(), 'First big right banner is not visible'

    def test_button_learn_more_in_long_term_care_section(self):
        homepage_nav = HomepageNav(self.driver)
        longtermcare_nav = LongTermCareNav(self.driver)
        button = homepage_nav.get_button_learn_more_in_long_term_care_section()
        homepage_nav.driver.execute_script("window.scrollBy(0,1000);")
        homepage_nav.hover_on_long_term_care_section()
        button.click()
        time.sleep(1)
        actual_title = longtermcare_nav.get_title_text()
        assert actual_title == "For Long Term Care"
