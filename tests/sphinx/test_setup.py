from bs4.element import Tag
import pytest

pytestmark = pytest.mark.sphinx('html', testroot='setup')


@pytest.mark.parametrize('page', ['index.html', ], indirect=True)
class TestSetupFunction:

    def test_index(self, page):
        element: Tag = page.select('.footer a')[1]
        content = element.contents[0].strip()
        assert 'Alabaster' in content
