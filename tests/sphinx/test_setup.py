from bs4.element import Tag
import pytest

pytestmark = pytest.mark.sphinx('html', testroot='setup')


@pytest.mark.parametrize('page', ['index.html', ], indirect=True)
class TestSetupFunction:

    def test_index(self, page):
        element: Tag = page.select_one('div')
        assert 'Hello f1' == element.text
