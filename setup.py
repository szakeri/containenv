from setuptools import setup, find_packages

import containenv

print(containenv.__version__)
setup(
    name='containenv',
    version=containenv.__version__,
    author='Za Wilgustus',
    author_email='wilcoxjg@gmail.com',
    license='Apache 2.0',
    url='https://github.com/zancas/containenv.git',
    packages=find_packages(),
    install_requires=['docker-py >= 1.10.6, < 1.11',
                      'jinja2 >= 2.8, < 3'],
    entry_points={'console_scripts': [
        'containenv=containenv.cli:main']},
    package_data={'containenv':['dockerfile_templates/*']}
)
