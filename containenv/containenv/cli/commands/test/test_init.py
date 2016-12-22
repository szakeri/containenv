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

from .....exceptions import ProjectAlreadyInitialized
from .....exceptions import ProjectDirectoryDoesNotExist
from ..init import Command as Init

logger = logging.getLogger(__name__)

def test__check_project_existence_no_dir(testdirectory):
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
    init_command = Init(testdirectory)
    init_command.make_path()
    assert init_command._check_project_existence() is None

def test__check_initialization_state_uninitialized(testdirectory):
    init_command = Init(testdirectory)
    init_command.make_path()
    assert init_command.check_initialization_state() is None

def test__check_initialization_state_initialized(testdirectory):
    EXTANTCONTAINENV = os.path.join(testdirectory, '.containenv')
    os.mkdir(EXTANTCONTAINENV)
    EXPECTED_ERROR = ('init can only be called once per project, but the {}\n'
                      'project already has a ".containenv" directory.'
                      ''.format(testdirectory))

    init_command = Init(testdirectory)
    init_command.make_path()
    if os.path.isdir(EXTANTCONTAINENV):
        print('IT EXISTS!')
        print(EXTANTCONTAINENV)
        print(init_command.proj_path)
    with pytest.raises(ProjectAlreadyInitialized) as PAIEIO:
        init_command.check_initialization_state()
    assert PAIEIO.value.args[0] == EXPECTED_ERROR

def test__catalog_languages_none():
    init_command = Init('PATHTOPYTHONDIR')

def test__catalog_languages_none_registered():
    init_command = Init('PATHTOPYTHONDIR')

def test__catalog_languages_pure_python_unregistered():
    init_command = Init('PATHTOPYTHONDIR')

def test__catalog_languages_bash_python():
    init_command = Init('PATHTOPYTHONDIR')

def test__catalog_languages_pure_go():
    init_command = Init('PATHTOPYTHONDIR')

def test__catalog_languages_bash_go():
    init_command = Init('PATHTOPYTHONDIR')

def test__render_config_config_invalid_missing():
    init_command = Init('PATHTOPYTHONDIR')
    
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
