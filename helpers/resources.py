import os
import tests


def path(app_package):
    return os.path.abspath(
        os.path.join(os.path.dirname(tests.__file__), f'../apps/{app_package}')
    )