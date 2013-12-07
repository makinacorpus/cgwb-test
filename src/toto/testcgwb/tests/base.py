import unittest2 as unittest

from toto.testcgwb.testing import (
    TOTO_TESTCGWB_FIXTURE as UNIT_TESTING,
    TOTO_TESTCGWB_INTEGRATION_TESTING as INTEGRATION_TESTING,
    TOTO_TESTCGWB_FUNCTIONAL_TESTING as FUNCTIONAL_TESTING,
)


class TestCase(unittest.TestCase):
    """We use this base class for all the tests in this package.
    If necessary, we can put common utility or setup code in here.
    """
    layer = UNIT_TESTING

    def setUp(self):
        super(TestCase, self).setUp()


class IntegrationTestCase(TestCase):
    """Integration base TestCase."""
    layer = INTEGRATION_TESTING


class FunctionalTestCase(TestCase):
    """Functionnal base TestCase."""
    layer = FUNCTIONAL_TESTING

# vim:set ft=python:
