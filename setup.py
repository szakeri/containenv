from setuptools import setup, find_packages

import containenv

print(containenv.__version__)
setup(
    name='containenv',
    version=containenv.__version__

)
