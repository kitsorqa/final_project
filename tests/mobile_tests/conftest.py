import pytest
from selene import browser, support
from utils import attachments
from selenium import webdriver
import allure
import allure_commons
import os
from appium.options.android import UiAutomator2Options

import config

from appium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        '--device_name',
        default='Google Pixel 3'
    )
    parser.addoption(
        "--context",
        required=False,
        default='bstack'
    )


@pytest.fixture(scope="function", autouse=True)
def browser_settings(request):
    device_name = request.config.getoption('--device_name')
    context = request.config.getoption('--context')

    print(context)

    capabilities = config.to_driver_options(context=context, device_name=device_name)

    if context == 'bstack':
        options = UiAutomator2Options().load_capabilities(capabilities).set_capability('app', os.getenv('app'))
    else:
        options = capabilities

    browser.config.timeout = float(os.getenv('timeout', '10.0'))

    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )
    with allure.step('init app session'):
        browser.config.driver = webdriver.Remote(options.get_capability('remote_url'), options=options)

    yield

    if context == 'bstack':
        attachments.add_screenshot(browser)
        # attaches.attach_xml(browser)
        session_id = browser.config.driver.session_id

        with allure.step('tear down app session'):
            browser.quit()

        attachments.attach_bstack_video(session_id)
