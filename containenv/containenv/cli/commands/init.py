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

'''
Usage: containenv init [metasource]

Options:
  -h, --help        Display this help message and exit.
'''
import os

from ....display import run_tasks


class Command(object):
    '''A containenv command that writes a container config and builds an image
    from it based on the current metasource directory.
    '''

    def __init__(self, metasource=os.curdir):
        self.metasource = os.path.abspath(metasource)
        self.tasks = [
            ('first thing', lambda: None),
            ('second thing', lambda: None),
            ('third thing', lambda: None),
            ]

    def __call__(self):
        """Write container config and build container .

        Returns:
            The exit code for the command, or None, implying a successful run.
        """
        return run_tasks(
            'running some tasks',
            self.tasks)
