"""
Run a Sphinx build with this theme and check the result.

"""

import pytest

pytestmark = pytest.mark.sphinx('html', testroot='setup')


@pytest.mark.parametrize('page', ['index.html', ], indirect=True)
class TestNullsterIndex:

    def test_index(self, page):
        assert 'Resource: Hello World' == page.select_one('h1').text
        assert 'Hello Nullster' == page.select_one('span').text


@pytest.mark.parametrize('page', ['_static/nullster.css', ], indirect=True)
class TestNullsterStatic:

    def test_static(self, page):
        assert 'body {}' == str(page)
