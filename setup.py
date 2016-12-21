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
                      'jinja2 >= 2.8, < 3',
                      'docopt >= 0.6.2, < 0.7',
                      'schema >= 0.6.5, < 0.7',
                      'colorama >= 0.3.7, < 0.4'],
    entry_points={'console_scripts': [
        'containenv=containenv.containenv.cli:main',
        'contain=containenv.contain.cli:main']},
    package_data={'containenv':['dockerfile_templates/*']}
)
