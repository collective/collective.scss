from collective.scss.tests import base

VARIABLES = """.content-navigation {
    border-color: #3bbfce;
    color: #2ba1af;}

.border {
    margin: 8px;
    padding: 8px;
    border-color: #3bbfce;}
"""
NESTING = """
table.hl {
    margin: 2em 0;}

table.hl td.ln {
    text-align: right;}

li {
    font-weight: bold;
    font-size: 1.2em;
    font-family: serif;}
"""
MIXINS = """#data {
    float: left;
    margin-left: 10px;}

#data th {
    text-align: center;
    font-weight: bold;}

#data td, #data th {
    padding: 2px;}
"""
SELECTOR_INHERITANCE = """
.error, .badError {
    border: 1px #f00;
    background: #fdd;}

.error.intrusion {
    font-weight: bold;
    font-size: 1.3em;}

.badError {
    border-width: 3px;}
"""

class TestStyleSheet(base.TestCase):

    def _callsheet(self, name):
        return self.portal.restrictedTraverse(name)()

    def test_variables(self):
        variables = self._callsheet('variables.scss')
        self.failUnless(variables == VARIABLES, variables)

    def test_nesting(self):
        nesting = self._callsheet('nesting.scss')
        self.failUnless(nesting == NESTING, nesting)

    def test_mixins(self):
        mixins = self._callsheet('mixins.scss')
        self.failUnless(mixins == MIXINS, mixins)

    def test_selector_inheritance(self):
        selector_inheritance = self._callsheet('selector-inheritance.scss')
        self.failUnless(selector_inheritance == SELECTOR_INHERITANCE, selector_inheritance)
