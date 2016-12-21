#!/usr/bin/env python

# Copyright 2016 F5 Networks Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from setuptools import find_packages
from setuptools import setup

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
    package_data={'containenv': ['dockerfile_templates/*']}
)
