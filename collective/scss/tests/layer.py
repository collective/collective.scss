from plone.testing import z2

from plone.app.testing import PloneSandboxLayer
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting, FunctionalTesting

class CollectiveLayer(PloneSandboxLayer):
    default_bases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import collective.scss
        import collective.scss.tests.example
        self.loadZCML(package=collective.scss)
        self.loadZCML(package=collective.scss.tests.example)

        # Install product and call its initialize() function
        z2.installProduct(app, 'collective.scss')

#    def setUpPloneSite(self, portal):
#        # Install into Plone site using portal_setup
#        self.applyProfile(portal, 'collective.gallery:default')

    def tearDownZope(self, app):
        # Uninstall product
        z2.uninstallProduct(app, 'collective.scss')

FIXTURE = CollectiveLayer()

INTEGRATION = IntegrationTesting(bases=(FIXTURE,), name="SCSS:Integration")
FUNCTIONAL = FunctionalTesting(bases=(FIXTURE,), name="SCSS:Functional")
