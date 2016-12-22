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
        self.metasource = metasource
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

    def make_path(self):
        '''construct target project path'''
        self.proj_path = os.path.abspath(self.metasource)

    def _check_project_existence(self):
        '''verify that self.proj_path is a valid project'''
        pass

    def check_initialization_state(self):
        '''determine whether a target project exists'''
        self._check_project_existence(self)
        # if .containenv....
        # raise AlreadyInitializedError

    def make_containenv_dir(self):
        '''make PROJECT/.containenv'''
        pass

    def _catalog_languages(self):
        '''create a list of languages used in the project'''
        pass

    def _render_config(self):
        '''produce a config file from the language catalog'''
        pass

    def _write_config(self):
        '''write the config to PROJECT/.containenv/Dockerfile?'''
        pass

    def write_container_config(self):
        '''create and write container config'''
        self._catalog_languages()
        self._render_config()
        self._write_config()

    def write_entrypoint(self):
        '''write the entrypoint script to PROJECT/.containenv/entrypoint.sh'''
        # All of the host environment should be ingested into the container
        pass

    def write_runcontainenv(self):
        '''write the runner script to PROJECT/.containenv/runcontainenv.sh'''
        # pass in all environment variables
        pass

    def _create_tag(self):
        '''create the correct tag'''
        self._sanitize_tag()
        self._prefix_registry()
        pass

    def build_image(self):
        '''from above results generate a tagged image'''
        pass

    def publish_image(self):
        '''if there's a shared registry publish to it'''
        pass
