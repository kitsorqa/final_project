import pytest
from selene import browser
from appium import webdriver
from config import config_mobile

from utils import attachments


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    options = config_mobile.get_options()
    browser.config.driver = webdriver.Remote(
        config_mobile.remote_url,
        options = options
    )
    browser.config.timeout = config_mobile.timeout

    yield

    attachments.attach_screenshot(browser)
    attachments.attach_xml_logs()

    session_id = browser.driver.session_id
    browser.quit()
    if config_mobile.context == 'bstack':
        attachments.bstack_video(session_id)