from Products.Five.browser import BrowserView

from scss import parser

class SCSSView(BrowserView):
    """SCSS base stylesheet view"""

    def __call__(self):
        # defer to index method, because that's what gets overridden by the template ZCML attribute
        scss = self.index().encode('utf-8')
        p = parser.Stylesheet()
        css = str(p.loads(scss))
        self.request.response.setHeader("Content-type", "text/css")
        return css

