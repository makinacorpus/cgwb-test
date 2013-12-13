import logging
from zope.i18nmessageid import MessageFactory

MessageFactory = testcgwbMessageFactory = MessageFactory('testcgwb')
logger = logging.getLogger('testcgwb')
EXTENSION_PROFILES = ('testcgwb:default',)
SKIN = 'skin'
PRODUCT_DEPENDENCIES = (
)


def initialize(context):
    """Initializer called when used as a Zope 2 product."""


GLOBALS = globals()
