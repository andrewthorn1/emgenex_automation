import time
import pytest
from pom.homepage_nav import HomepageNav
from pom.getintouchpage_nav import GetInTouchNav


@pytest.mark.smoke
@pytest.mark.usefixtures('setup')
class TestGetInTouch:

    @pytest.mark.regression
    def test_with_all_required_fields(self):
        homepage_nav = HomepageNav(self.driver)
        getintouch_nav = GetInTouchNav(self.driver)
        homepage_nav.get_contact_us_link().click()
        getintouch_nav.get_first_name_field().send_keys("Test FirstName")
        getintouch_nav.get_last_name_field().send_keys("Test LastName")
        getintouch_nav.get_email_field().send_keys("testemail@gmail.com")
        getintouch_nav.driver.execute_script("window.scrollBy(0,300);")
        time.sleep(1)
        getintouch_nav.get_radio_button_no().click()
        getintouch_nav.get_submit_button().click()
        actual_message_text = getintouch_nav.get_submitted_message_text()
        assert actual_message_text == "Thanks for submitting the form.", "Problems with Get In Touch form"

    @pytest.mark.regression
    def test_with_not_all_required_fields(self):
        homepage_nav = HomepageNav(self.driver)
        getintouch_nav = GetInTouchNav(self.driver)
        homepage_nav.get_contact_us_link().click()
        getintouch_nav.get_first_name_field().send_keys("Test FirstName")
        getintouch_nav.get_last_name_field().send_keys("Test LastName")
        getintouch_nav.get_submit_button().click()
        actual_error_text = getintouch_nav.get_error_message_text()
        assert actual_error_text == "Please complete all required fields."
