"""
Launching all doctests in the tests directory using:

    - the base layer in testing.py

"""

import unittest2 as unittest
import glob
import os
import logging
import doctest
from plone.testing import layered


def get_globs():
    """
    GLOBALS avalaible in doctests
    """
    globs = globals()
    globs.update(locals())
    return globs

# example:
# from for import bar
# and in your doctests, you can do:
# >>> bar.something
from testcgwb.testing import TESTCGWB_FUNCTIONAL_TESTING as FUNCTIONAL_TESTING

optionflags = (doctest.ELLIPSIS
               | doctest.NORMALIZE_WHITESPACE
               | doctest.REPORT_ONLY_FIRST_FAILURE)


def test_suite():
    """."""
    logger = logging.getLogger('testcgwb.tests')
    cwd = os.path.dirname(__file__)
    files = []
    try:
        files = []
        for e in ['*rst', '*txt']:
            for d in [cwd,
                      os.path.dirname(cwd)]:
                files += glob.glob(os.path.join(d, e))
    except Exception:
        logger.warn('No doctests for testcgwb')
    suite = unittest.TestSuite()
    globs = get_globs()
    for s in files:
        suite.addTests([
            layered(
                doctest.DocFileSuite(
                    s,
                    globs=globs,
                    module_relative=False,
                    optionflags=optionflags,
                ),
                layer=FUNCTIONAL_TESTING
            ),
        ])
    return suite
