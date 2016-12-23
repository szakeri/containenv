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
import collections
import os
import logging
from pprint import pprint as pp
import site
import sys

from containenv.config.dependencymaps import EXTENSION_MAP
from containenv.config.dependencymaps import FILENAME_MAP
from containenv.config.dependencymaps import DIRNAME_MAP
from containenv.display import run_tasks
from containenv.exceptions import ProjectAlreadyInitialized
from containenv.exceptions import ProjectDirectoryDoesNotExist
from containenv.exceptions import ProjectContainsNoRegisteredNodes


logger = logging.getLogger(__name__)

class Command(object):
    '''A containenv command that writes a container config and builds an image
    from it based on the current metasource directory.
    '''

    def __init__(self, metasource=os.curdir):
        self.metasource = metasource
        logger.warning('self.metasource: {}'.format(self.metasource))
        self.tasks = [self._make_task(m) for m in [
            self.make_path,
            self.check_initialization_state,
            self.make_containenv_dir,
            self.write_container_config,
            self.write_entrypoint,
            self.write_runcontainenv,
            self.build_image,
            self.publish_image]]

    def __call__(self):
        """Write container config and build container .

        Returns:
            The exit code for the command, or None, implying a successful run.
        """
        return run_tasks(
            'running some tasks',
            self.tasks)

    def _make_task(self, method):
        '''create a run_tasks compliant task'''
        return (method.__doc__, method)

    def make_path(self):
        '''construct target project path'''
        self.proj_path = os.path.abspath(self.metasource)

    def _check_project_existence(self):
        '''verify that self.proj_path is a valid project'''
        if not os.path.isdir(self.proj_path):
            error = ('init must be called on a project directory but the '
                     'argument it received was: {}\nwhich does not map to '
                     'a path to an existing directory.'
                     ''.format(self.metasource))
            raise ProjectDirectoryDoesNotExist(error)

    def check_initialization_state(self):
        '''determine whether a target project exists'''
        self._check_project_existence()
        print('THE PROJECT EXISTS')
        if os.path.isdir(os.path.join(self.proj_path, '.containenv')):
            error = ('init can only be called once per project, but the {}\n'
                     'project already has a ".containenv" directory.'
                     ''.format(self.proj_path))
            raise ProjectAlreadyInitialized(error)

    def make_containenv_dir(self):
        '''make PROJECT/.nenv'''
        self.containenvdir = os.path.join(self.proj_path, '.containenv')
        os.mkdir(self.containenvdir)

    def _register_file(self, dirpath, fname, extension):
        pp(extension)
        # First use file extensions
        if extension in EXTENSION_MAP:
            self.registered_dependency_catalog[EXTENSION_MAP[extension]]\
               .add(os.path.join(dirpath, fname+extension))
        # Then check against fnames
        elif fname in FILENAME_MAP:
            self.registered_dependency_catalog[FILENAME_MAP[fname]]\
               .add(os.path.join(dirpath, fname+extension))
        else:
            self.unregistered_nodes.add(os.path.join(dirpath, fname+extension))

    def _register_dir(self, dirpath):
        if dirpath in DIRNAME_MAP:
            self.registered_dependency_catalog[DIRNAME_MAP[dirpath]].add(dirpath)
        else:
            self.unregistered_nodes.add(dirpath)

    def _catalog_dependencies(self):
        '''create a list of technologies used in the project'''
        
        self.registered_dependency_catalog = collections.defaultdict(set)
        self.unregistered_nodes = set()
        print('self.registered_dependency_catalog is {}'.format(self.registered_dependency_catalog))
        pp(EXTENSION_MAP)
        for dirpath, dirs, files in os.walk(self.proj_path):
            pp(files)
            for fname, extension in [os.path.splitext(f) for f in files]:
                self._register_file(dirpath, fname, extension)
            self._register_dir(dirpath)
        pp(self.registered_dependency_catalog)
        if not self.registered_dependency_catalog:
            error = ('None of the nodes (files and directories) in this'
                     ' project are registered with containenv.')
            raise ProjectContainsNoRegisteredNodes(error)

    def _render_config(self):
        '''produce a config file from the language catalog'''
        pass

    def _write_config(self):
        '''write the config to PROJECT/.containenv/Dockerfile?'''
        pass

    def write_container_config(self):
        '''create and write container config'''
        self._catalog_dependencies()
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

    def _sanitize_tag(self):
        '''the result must be a valid image tag'''
        pass

    def _prefix_registry(self):
        '''the result must have the correct registry prefix'''
        pass

    def _create_tag(self):
        '''create the correct tag'''
        self._sanitize_tag()
        self._prefix_registry()
        pass

    def build_image(self):
        '''from above results generate a tagged image'''
        self._create_tag()        

    def publish_image(self):
        '''if there's a shared registry publish to it'''
        pass
