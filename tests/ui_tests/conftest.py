import pytest
import os
from selene import browser
from utils import attachments
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function", autouse=True)
def browser_settings():
    selenoid_login = os.getenv("SELENOID_LOGIN")
    selenoid_pass = os.getenv("SELENOID_PASSWORD")
    selenoid_url = os.getenv("SELENOID_URL")
    browser.config.window_height = 1080
    browser.config.window_width = 1920
    browser.config.base_url = 'https://yasno.live'
    browser.config.timeout = 15

    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "127.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--incognito")

    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub",
        options=options
    )
    browser.config.driver = driver

    yield

    attachments.add_html(browser)
    attachments.attach_screenshot(browser)
    attachments.add_logs()
    attachments.add_video(browser)

    browser.quit()
