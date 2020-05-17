from bs4.element import Tag
import pytest

pytestmark = pytest.mark.sphinx('html', testroot='hello-resource')


@pytest.mark.parametrize('page', ['index.html', ], indirect=True)
class TestHelloResourceFunction:

    def test_index(self, page):
        heading: Tag = page.select_one('h1')
        assert 'index' == heading.text
        body: Tag = page.select_one('div')
        assert 'Hello World' in body.text
