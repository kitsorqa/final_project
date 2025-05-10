import os
from pathlib import Path

from helpers import resources
from dotenv import load_dotenv
from pydantic.v1 import BaseSettings
from appium.options.android import UiAutomator2Options

load_dotenv()

class ProjectConfig(BaseSettings):
    context = "bstack"
    platformName: str
    bstack_userName: str = None
    bstack_accessKey: str = None
    app_package: str
    remote_url: str = 'http://hub.browserstack.com/wd/hub'
    deviceName: str
    platformVersion: str = None
    timeout: int = 25

    def get_options(self):
        capabilities = {
            'platformVersion': self.platformVersion,
            'deviceName': self.deviceName,
            'app': config_mobile.app_package if config_mobile.app_package.startswith('bs://') else resources.path(self.app_package)
            #'appWaitActivity': "live.yasno.app"
        }

        if self.context == 'bstack':
            capabilities['bstack:options'] = {
                'projectName': 'Mobile project',
                'buildName': 'browserstack-build-1',
                'sessionName': f'{self.platformName} test',
                'userName': self.bstack_userName,
                'accessKey': self.bstack_accessKey,
            }

        if self.platformName == 'android':
            return UiAutomator2Options().load_capabilities(capabilities)


def get_config():
    context = os.getenv('context', 'bstack')
    load_dotenv(dotenv_path = f'.env.{context}')
    if context == 'bstack':
        load_dotenv(dotenv_path = Path('.env'), override = True)
    local_config = ProjectConfig(_env_file=Path(f'.env.{context}'))
    local_config.context = context
    return local_config


config_mobile = get_config()