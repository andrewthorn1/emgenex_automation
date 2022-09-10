import time
import pytest
from pom.homepage_nav import HomepageNav


@pytest.mark.usefixtures('setup')
class TestGetStartForm:

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_with_all_required_fields(self):
        homepage_nav = HomepageNav(self.driver)
        homepage_nav.driver.execute_script("window.scrollBy(0,4600);")
        homepage_nav.get_first_name_field().send_keys("Test FirstName")
        homepage_nav.get_last_name_field().send_keys("Test LastName")
        homepage_nav.get_email_field().send_keys("testemail@gmail.com")
        homepage_nav.get_submit_button().click()
        actual_message_text = homepage_nav.get_submitted_message_text()
        assert actual_message_text == "Thanks for submitting the form.", "Problems with Get Started form"

    @pytest.mark.regression
    def test_with_all_required_fields(self):
        homepage_nav = HomepageNav(self.driver)
        homepage_nav.driver.execute_script("window.scrollBy(0,4600);")
        homepage_nav.get_first_name_field().send_keys("Test FirstName")
        homepage_nav.get_last_name_field().send_keys("Test LastName")
        homepage_nav.get_submit_button().click()
        actual_error_text = homepage_nav.get_error_message_text()
        assert actual_error_text == "Please complete all required fields."
