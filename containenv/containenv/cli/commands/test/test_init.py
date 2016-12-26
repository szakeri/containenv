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
import logging
import os

import pytest

from containenv.exceptions import ProjectAlreadyInitialized,\
                                  ProjectDirectoryDoesNotExist,\
                                  ProjectContainsNoRegisteredNodes
from containenv.containenv.cli.commands.init import Command as Init

logger = logging.getLogger(__name__)

# tests pre self.make_containenv_dir
def test__check_project_existence_no_dir(testdirectory):
    '''The argument does not a even correspond to a directory.'''
    NONEXTANTDIR = os.path.join(testdirectory, 'NONE')
    EXPECTED_ERROR = ('init must be called on a project directory but the'
                      ' argument it received was: {}\nwhich does not map to a'
                      ' path to an existing directory.'.format(NONEXTANTDIR))
    init_command = Init(NONEXTANTDIR)
    init_command.make_path()
    with pytest.raises(ProjectDirectoryDoesNotExist) as PDDNEEIO:
        init_command._check_project_existence()
    assert PDDNEEIO.value.args[0] == EXPECTED_ERROR
    
def test__check_project_existence_dir(testdirectory):
    '''The argument does correspond to a directory.'''
    init_command = Init(testdirectory)
    init_command.make_path()
    assert init_command._check_project_existence() is None

def test__check_initialization_state_uninitialized(testdirectory):
    '''The argument does not _already_ possess a ".containenv".'''
    init_command = Init(testdirectory)
    init_command.make_path()
    assert init_command.check_initialization_state() is None

# tests post self.make_containenv_dir
@pytest.fixture
def testdirskeleton(testdirectory):
    SUBDIRPATH = os.path.join(testdirectory, 'SUB')
    os.mkdir(SUBDIRPATH)
    init_command = Init(testdirectory)
    init_command.make_path()
    init_command.make_containenv_dir()
    return testdirectory, init_command.containenvdir, SUBDIRPATH, init_command

def test__check_initialization_state_already_initialized(testdirskeleton):
    '''The argument _already_ (incorrectly) possesses a ".containenv".'''
    testdirectory, CONTAINENVPATH, SUBDIRPATH, init_command = testdirskeleton
    EXPECTED_ERROR = ('init can only be called once per project, but the {}\n'
                      'project already has a ".containenv" directory.'
                      ''.format(testdirectory))
    with pytest.raises(ProjectAlreadyInitialized) as PAIEIO:
        init_command.check_initialization_state()
    assert PAIEIO.value.args[0] == EXPECTED_ERROR

def test__catalog_dependencies_none_registered(testdirskeleton):
    '''none of the nodes are registered as containenv dependencies'''
    testdirectory, CONTAINENVPATH, SUBDIRPATH, init_command = testdirskeleton
    EXPECTED_UNREGISTERED = {SUBDIRPATH, CONTAINENVPATH}
    fnames = [os.path.join(testdirectory, n) for n in [
                os.path.join(SUBDIRPATH, 'foo.txt'),
                'setup.cfg',
                'setup']] 
    for fn in fnames:
        open(fn, 'w').write('TESTTEXT')
        EXPECTED_UNREGISTERED.add(fn)
    with pytest.raises(ProjectContainsNoRegisteredNodes) as PCNRNEIO:
        init_command._catalog_dependencies()
    assert init_command.unregistered_nodes == EXPECTED_UNREGISTERED
    assert PCNRNEIO.value.args[0] == \
        ('None of the nodes (files and directories) in this project are'
         ' registered with containenv.')

@pytest.fixture
def testdirgeneric(testdirskeleton):
    testdirectory, CONTAINENVPATH, SUBDIRPATH, init_command = testdirskeleton
    gitdirpath = os.path.join(testdirectory, '.git')
    os.mkdir(gitdirpath)
    fnames = [os.path.join(testdirectory, n) for n in [
                os.path.join(SUBDIRPATH, 'foo.go'),
                'Makefile.build',
                'setup.sh',
                'py.foo',
                os.path.join(gitdirpath, 'didntgetregistered.py')]] 
    for fn in fnames:
        open(fn, 'w').write('TESTTEXT')
    return (testdirectory,
            CONTAINENVPATH,
            SUBDIRPATH,
            init_command,
            gitdirpath,
            fnames)

def test__catalog_dependencies_bash_go_git_makefile(testdirgeneric):
    (testdirectory,
    CONTAINENVPATH,
    SUBDIRPATH,
    init_command,
    gitdirpath,
    fnames) = testdirgeneric
    EXPECTED_UNREGISTERED = {testdirectory, SUBDIRPATH, CONTAINENVPATH}
    init_command._catalog_dependencies()
    assert init_command.registered_dependency_catalog.pop('go') ==\
        set([fnames[0]])
    assert init_command.registered_dependency_catalog.pop('make') ==\
        set([fnames[1]])
    assert init_command.registered_dependency_catalog.pop('shell') ==\
        set([fnames[2]])
    assert init_command.registered_dependency_catalog.pop('git') ==\
        set([gitdirpath])
    assert not init_command.registered_dependency_catalog
    assert init_command.unregistered_nodes ==\
        {fnames[3], SUBDIRPATH, CONTAINENVPATH}

def test__render_config_config_invalid_missing(testdirskeleton):
    testdirectory, CONTAINENVPATH, SUBDIRPATH, init_command = testdirskeleton
    
def test__render_config_config_invalid_unexpected():
    init_command = Init('PATHTOPYTHONDIR')
    
def test_write_container_config():
    init_command = Init('PATHTOPYTHONDIR')
    
def test_write_entrypoint():
    init_command = Init('PATHTOPYTHONDIR')

def test_write_runcontainenv():
    init_command = Init('PATHTOPYTHONDIR')

def test__create_tag_noreg_notaginvalid_chars():
    init_command = Init('PATHTOPYTHONDIR')

def test__create_tag_noreg_taginvalid_chars():
    init_command = Init('PATHTOPYTHONDIR')

def test__create_tag_reg_notaginvalid_chars():
    init_command = Init('PATHTOPYTHONDIR')

def test__create_tag_reg_taginvalid_chars():
    init_command = Init('PATHTOPYTHONDIR')

def test_build_image():
    init_command = Init('PATHTOPYTHONDIR')
