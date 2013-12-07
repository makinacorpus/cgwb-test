"""
Plone.testing is a testing framework, it is not related to plone
"""
from plone.testing.layer import Layer as Base


def print_contents(browser, dest='~/.browser.html'):
    """Print the browser contents somewhere for you to see its context
    in doctest pdb, type print_contents(browser) and that's it, open firefox
    with file://~/browser.html."""
    import os
    open(os.path.expanduser(dest), 'w').write(browser.contents)


class Layer(Base):

    defaultBases = tuple()


TATA_TOTO_TESTCGWB_FIXTURE = Layer()


class IntegrationLayer(Layer):
    """."""
    defaultBases = (TATA_TOTO_TESTCGWB_FIXTURE,)


class FunctionnalLayer(IntegrationLayer):
    """."""
    defaultBases = (TATA_TOTO_TESTCGWB_FIXTURE,)

TATA_TOTO_TESTCGWB_INTEGRATION_TESTING = IntegrationLayer()
TATA_TOTO_TESTCGWB_FUNCTIONAL_TESTING = FunctionnalLayer()
