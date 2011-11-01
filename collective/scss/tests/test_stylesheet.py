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

def are_same_styles(s1,s2):
    clean1 = s1.replace('\n','').replace(' ','').replace('\t','')
    clean2 = s2.replace('\n','').replace(' ','').replace('\t','')
    return clean1 == clean2

class TestStyleSheet(base.TestCase):

    def _callsheet(self, name):
        return self.portal.restrictedTraverse(name)()

    def test_variables(self):
        variables = self._callsheet('variables.scss')
        self.failUnless(are_same_styles(variables, VARIABLES))

    def test_nesting(self):
        nesting = self._callsheet('nesting.scss')
        self.failUnless(are_same_styles(nesting, NESTING))

    def test_mixins(self):
        mixins = self._callsheet('mixins.scss')
        self.failUnless(are_same_styles(mixins, MIXINS))

    def test_selector_inheritance(self):
        selector_inheritance = self._callsheet('selector-inheritance.scss')
        self.failUnless(are_same_styles(selector_inheritance, SELECTOR_INHERITANCE))
