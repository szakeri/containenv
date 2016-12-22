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

from .....exceptions import ProjectDirectoryDoesNotExist
from ..init import Command

logger = logging.getLogger(__name__)

def test__check_project_existence_no_dir(testdirectory):
    NONEXTANTDIR = os.path.join(testdirectory, 'NONE')
    EXPECTED_ERROR = ('init must be called on a project directory but the'
                      ' argument it received was: {}\nwhich does not map to a'
                      ' path to an existing directory.'.format(NONEXTANTDIR))
    c = Command(NONEXTANTDIR)
    c.make_path()
    with pytest.raises(ProjectDirectoryDoesNotExist) as PDDNEEIO:
        c._check_project_existence()
    assert PDDNEEIO.value.args[0] == EXPECTED_ERROR
    

def test__check_project_existence_dir(testdirectory):
    c = Command(testdirectory)
    c.make_path()
    assert c._check_project_existence() is None

def test__check_initialization_state_uninitialized():
    c = Command('PATHTOUNINITDIR')

def test__check_initialization_state_initialized():
    c = Command('PATHTOINITDIR')

def test__catalog_languages_none():
    c = Command('PATHTOPYTHONDIR')

def test__catalog_languages_none_registered():
    c = Command('PATHTOPYTHONDIR')

def test__catalog_languages_pure_python_unregistered():
    c = Command('PATHTOPYTHONDIR')

def test__catalog_languages_bash_python():
    c = Command('PATHTOPYTHONDIR')

def test__catalog_languages_pure_go():
    c = Command('PATHTOPYTHONDIR')

def test__catalog_languages_bash_go():
    c = Command('PATHTOPYTHONDIR')

def test__render_config_config_invalid_missing():
    c = Command('PATHTOPYTHONDIR')
    
def test__render_config_config_invalid_unexpected():
    c = Command('PATHTOPYTHONDIR')
    
def test_write_container_config():
    c = Command('PATHTOPYTHONDIR')
    
def test_write_entrypoint():
    c = Command('PATHTOPYTHONDIR')

def test_write_runcontainenv():
    c = Command('PATHTOPYTHONDIR')

def test__create_tag_noreg_notaginvalid_chars():
    c = Command('PATHTOPYTHONDIR')

def test__create_tag_noreg_taginvalid_chars():
    c = Command('PATHTOPYTHONDIR')

def test__create_tag_reg_notaginvalid_chars():
    c = Command('PATHTOPYTHONDIR')

def test__create_tag_reg_taginvalid_chars():
    c = Command('PATHTOPYTHONDIR')

def test_build_image():
    c = Command('PATHTOPYTHONDIR')
