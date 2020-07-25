from markupsafe import Markup

from themester.sphinx.documentbody import DocumentBody


def test_construction():
    """ Barely useful, just ensure the API """

    html = Markup('<p>Some text</p>')
    db = DocumentBody(html=html)
    assert '<p>Some text</p>' == db.html
