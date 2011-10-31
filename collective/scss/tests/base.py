import unittest2 as unittest
from zope import interface
from plone.app import testing
from collective.scss.tests import layer
from collective.scss.tests import utils

class UnitTestCase(unittest.TestCase):
    
    def setUp(self):
        from ZPublisher.tests.testPublish import Request
        super(UnitTestCase, self).setUp()
        self.context = utils.FakeContext()
        self.request = Request()

class TestCase(unittest.TestCase):

    layer = layer.INTEGRATION

    def setUp(self):
        from zope.annotation.interfaces import IAttributeAnnotatable
        interface.alsoProvides(self.layer['request'],
                               (IAttributeAnnotatable,))
        super(TestCase, self).setUp()
        self.portal = self.layer['portal']
        testing.setRoles(self.portal, testing.TEST_USER_ID, ['Manager'])
        self.portal.invokeFactory('Folder', 'test-folder')
        testing.setRoles(self.portal, testing.TEST_USER_ID, ['Member'])
        self.folder = self.portal['test-folder']

class FunctionalTestCase(unittest.TestCase):

    layer = layer.FUNCTIONAL

    def setUp(self):
        from zope.annotation.interfaces import IAttributeAnnotatable
        interface.alsoProvides(self.layer['request'],
                               (IAttributeAnnotatable,))
        self.portal = self.layer['portal']
        testing.setRoles(self.portal, testing.TEST_USER_ID, ['Manager'])
        self.portal.invokeFactory('Folder', 'test-folder')
        testing.setRoles(self.portal, testing.TEST_USER_ID, ['Member'])
        self.folder = self.portal['test-folder']

def build_test_suite(test_classes):
    suite = unittest.TestSuite()
    for klass in test_classes:
        suite.addTest(unittest.makeSuite(klass))
    return suite
