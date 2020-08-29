import pytest
from bs4.element import Tag

pytestmark = pytest.mark.sphinx('html', testroot='autodoc')


@pytest.mark.parametrize('page', ['index.html', ], indirect=True)
class TestAutodocIndex:
    """ Home page of a site with autodoc """

    def test_api(self, page):
        title = page.select_one('title').contents[0].strip()
        assert 'Welcome To My Project - Python' == title
        links = page.select('.toctree-wrapper a')
        assert 2 == len(links)
        assert 'API' == links[0].text
        assert 'Module contents' == links[1].text


@pytest.mark.parametrize('page', ['api.html', ], indirect=True)
class TestAutodocApi:
    """ Ensure we don't break generation of autodoc """

    def test_api(self, page):
        api: Tag = page.select_one('#module-foo')
        assert api

        assert 'API - Python' == page.select_one('title').text
        assert 'Module contents¶' == api.select_one('h2').text
        assert '#module-foo' == api.select_one('h2 a')['href']

        dt: Tag = page.find('dt', attrs=dict(id='foo.bar'))
        assert dt
        assert 'foo.' == dt.select_one('.descclassname').text
        assert 'bar' == dt.select_one('.descname').text
        assert '(' == dt.select_one('.sig-paren').text
        assert ')' == dt.select('.sig-paren')[1].text
        assert '#foo.bar' == dt.select_one('a')['href']
        assert 'msg: str' == dt.select_one('.sig-param').text
