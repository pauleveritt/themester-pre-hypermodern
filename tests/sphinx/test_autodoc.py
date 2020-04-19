import pytest
from bs4.element import Tag

pytestmark = pytest.mark.sphinx('html', testroot='autodoc')


@pytest.mark.parametrize('page', ['api.html', ], indirect=True)
class TestAutodoc:
    """ Ensure we don't break generation of autodoc """

    def test_api(self, page):
        api: Tag = page.select_one('#module-foo')
        assert api

        assert 'Module contents¶' == api.select_one('h2').text
        assert '#module-foo' == api.select_one('h2 a')['href']

        dt: Tag = page.find('dt', attrs=dict(id='foo.bar'))
        assert dt
        assert 'foo.' == dt.select_one('.descclassname').text
        assert 'bar' == dt.select_one('.descname').text
        assert '(' == dt.select_one('.sig-paren').text
        assert ')' == dt.select('.sig-paren')[1].text
        assert '#foo.bar' == dt.select_one('a')['href']
