# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4
#
# Copyright (C) 2010-2016 GEM Foundation
#
# OpenQuake is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# OpenQuake is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with OpenQuake. If not, see <http://www.gnu.org/licenses/>.

"""
Helper functions for our unit and smoke tests.
"""
import functools
import mock as mock_module
import os
import random
import shutil
import string
import tempfile
import textwrap

from openquake.baselib.general import writetmp as touch
from openquake.commonlib import config
from openquake.engine import engine

CD = os.path.dirname(__file__)  # current directory

RUNNER = os.path.abspath(os.path.join(CD, '../../../bin/oq'))

DATA_DIR = os.path.abspath(os.path.join(CD, './data'))

OUTPUT_DIR = os.path.abspath(os.path.join(CD, './data/output'))


#: Wraps mock.patch() to make mocksignature=True by default.
patch = functools.partial(mock_module.patch, mocksignature=True)


def default_user():
    """Return the default user to be used for test setups."""
    return "openquake"


def _patched_mocksignature(func, mock=None, skipfirst=False):
    """
    Fixes arguments order and support of staticmethods in mock.mocksignature.
    """
    static = False
    if isinstance(func, staticmethod):
        static = True
        func = func.__func__

    if mock is None:
        mock = mock_module.Mock()
    signature, func = mock_module._getsignature(func, skipfirst)

    checker = eval("lambda %s: None" % signature)
    mock_module._copy_func_details(func, checker)

    def funcopy(*args, **kwargs):
        checker(*args, **kwargs)
        return mock(*args, **kwargs)

    if not hasattr(mock_module, '_setup_func'):
        # compatibility with mock < 0.8
        funcopy.mock = mock
    else:
        mock_module._setup_func(funcopy, mock)
    if static:
        funcopy = staticmethod(funcopy)
    return funcopy
mock_module.mocksignature = _patched_mocksignature


def get_data_path(file_name):
    return os.path.join(DATA_DIR, file_name)


def run_job(cfg, exports='xml,csv', hazard_calculation_id=None, **params):
    """
    Given the path to a job config file and a hazard_calculation_id
    or a output, run the job.

    :returns: a calculator object
    """
    job_id, oqparam = engine.job_from_file(
        cfg, 'openquake', 'error', [], hazard_calculation_id, **params)
    logfile = os.path.join(tempfile.gettempdir(), 'qatest.log')
    return engine.run_calc(job_id, oqparam, 'error', logfile, exports)


class ConfigTestCase(object):
    """Class which contains various configuration- and environment-related
    testing helpers."""

    def setup_config(self):
        self.orig_env = os.environ.copy()
        os.environ.clear()
        # Move the local configuration file out of the way if it exists.
        # Otherwise the tests that follow will break.
        local_path = "%s/openquake.cfg" % os.path.abspath(config.OQDIR)
        if os.path.isfile(local_path):
            shutil.move(local_path, "%s.test_bakk" % local_path)

    def teardown_config(self):
        os.environ.clear()
        os.environ.update(self.orig_env)
        # Move the local configuration file back into place if it was stashed
        # away.
        local_path = "%s/openquake.cfg" % os.path.abspath(config.OQDIR)
        if os.path.isfile("%s.test_bakk" % local_path):
            shutil.move("%s.test_bakk" % local_path, local_path)
        config.cfg.cfg.clear()
        config.cfg._load_from_file()

    def prepare_config(self, section, data=None):
        """Set up a configuration with the given `max_mem` value."""
        if data is not None:
            data = '\n'.join("%s=%s" % item for item in data.items())
            content = """
                [%s]
                %s""" % (section, data)
        else:
            content = ""
        site_path = touch(content=textwrap.dedent(content))
        os.environ["OQ_SITE_CFG_PATH"] = site_path
        config.cfg.cfg.clear()
        config.cfg._load_from_file()


def random_string(length=16):
    """Generate a random string of the given length."""
    result = ""
    while len(result) < length:
        result += random.choice(string.ascii_letters + string.digits)
    return result
