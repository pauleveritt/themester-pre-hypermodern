"""

Test the optional sidebars in the basic theme as well as the modindex
and other generated pages.

"""
import pytest
from bs4.element import Tag

pytestmark = pytest.mark.sphinx('html', testroot='basic-sidebars')


@pytest.mark.parametrize('page', ['subdir/subfile.html', ], indirect=True)
class TestBasicSidebars:
    """ Turn on the optional html_sidebars in the basic theme """

    def test_globaltoc(self, page):
        globaltoc: Tag = page.find('div', attrs={'data-testid': 'globaltoc-heading'})
        a: Tag = globaltoc.find('a')
        assert '../index.html' == a['href']
        assert 'Table of Contents' == a.text

    def test_sourcelink(self, page):
        sourcelink: Tag = page.find('div', attrs={'data-testid': 'sourcelink'})
        assert 'This Page' == sourcelink.find('h3').text
        links: Tag = sourcelink.find_all('a')
        assert 1 == len(links)
        assert '../_sources/subdir/subfile.rst.txt' == links[0]['href']
        assert 'Show Source' == links[0].text

    def test_searchbox(self, page):
        searchbox: Tag = page.find('div', attrs={'data-testid': 'searchbox'})
        assert 'Quick search' == searchbox.find('h3').text
