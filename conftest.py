import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options as chrome_options
import os

TEST_ENVIRONMENT = os.environ.get('TEST_ENVIRONMENT')

@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_argument('chrome')  # Use headless if you don't need a browser UI
    options.add_experimental_option('excludeSwitches', ['enable-logging']) #make report without 'DevTools listening on ws://127.0.0.1:...'
    options.add_argument('--start-maximized')
    options.add_argument('--window-size=1650,900')
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    if TEST_ENVIRONMENT == 'docker':
        # driver = webdriver.Remote("http://browser:4444/wd/hub", DesiredCapabilities.FIREFOX)
        driver = webdriver.Remote("http://selenium:4444/wd/hub", DesiredCapabilities.CHROME)
    else:
        options = get_chrome_options
        driver = webdriver.Chrome(options=options)
    return driver


@pytest.fixture(scope='function')
def setup(request, get_webdriver):
    driver = get_webdriver
    url = "https://www.emgenex.com/"
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    driver.delete_all_cookies()
    yield driver
    driver.quit()


