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
import pytest

import shutil
import tempfile

@pytest.fixture
def testdirectory(request):
    tempdir = tempfile.mkdtemp()
    def rm_rf_dir():
        print(tempdir)
        shutil.rmtree(tempdir)
    request.addfinalizer(rm_rf_dir)
    return tempdir
