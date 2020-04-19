import pytest
from bs4.element import Tag

pytestmark = pytest.mark.sphinx('html', testroot='alabaster-hiderelated')


@pytest.mark.parametrize('css', ['_static/goku.css', ], indirect=True)
class TestAlabasterHideRelated:
    """ Make sure the CSS reflects this knob change """

    def test_css(self, css):
        assert 'div.relations' not in css
