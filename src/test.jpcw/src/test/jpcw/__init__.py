import logging
from zope.i18nmessageid import MessageFactory

MessageFactory = testjpcwMessageFactory = MessageFactory('test.jpcw')
logger = logging.getLogger('test.jpcw')
EXTENSION_PROFILES = ('test.jpcw:default',)
SKIN = 'test.skin'
PRODUCT_DEPENDENCIES = (
)


def initialize(context):
    """Initializer called when used as a Zope 2 product."""


GLOBALS = globals()
