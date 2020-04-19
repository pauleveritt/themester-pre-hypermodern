import pytest
from bs4.element import Tag

# The default values for all theme options, knobs, templates, etc.
# Nothing customized in conf.py or anywhere else.

pytestmark = pytest.mark.sphinx('html', testroot='alabaster-sidebars')


# *** NOTE: We are using ``subdir/subfile.html`` to get some of the
# navigation in the sidebars.
@pytest.mark.parametrize('page', ['subdir/subfile.html', ], indirect=True)
class TestAlabasterSidebars:
    """ Turn on the Alabaster-recommended html_sidebars """

    def test_html_title(self, page):
        """ Test the global conf value html_title """

        # The conf file sets html_title to None, which should turn
        # off the suffic addition to <title>
        title: Tag = page.find('title')
        assert 'Subfile' == title.text

    def test_about_logo(self, page):
        logo: Tag = page.select_one('p.logo')
        assert logo

        # The href on the link
        assert '../index.html' == logo.find('a')['href']

        # img path
        assert '../_static/python-logo.png' == logo.find('img')['src']

        # heading
        assert 'Goku Sidebars' == logo.find('h1').text

    def test_about_description(self, page):
        assert 'description1' == page.select_one('p.blurb').text

    def test_github(self, page):
        github: Tag = page.find('iframe', attrs=dict(width='200px'))
        assert 'github_user1' in github['src']
        assert 'github_repo1' in github['src']
        assert 'github_type1' in github['src']
        assert 'github_count1' in github['src']

    def test_about_travis(self, page):
        travis: Tag = page.select('a.badge')[0]
        assert 'travis-ci.org' in travis['href']
        assert 'github_user1' in travis['href']
        assert 'badge_branch1' in travis.select_one('img')['alt']
        assert 'badge_branch1' in travis.select_one('img')['src']

    def test_about_codecov(self, page):
        travis: Tag = page.select('a.badge')[1]
        assert 'codecov.io' in travis['href']
        assert 'github_user1' in travis['href']
        assert 'badge_branch1' in travis.select_one('img')['alt']
        assert 'badge_branch1' in travis.select_one('img')['src']

    def test_donate_heading(self, page):
        heading: Tag = page.select_one('h3.donation')
        assert heading

    def test_donate_url(self, page):
        link: Tag = page.find('a', attrs=dict(href='donate_url1'))
        assert link
        assert 'shields.io' in link.select_one('img')['src']

    def test_donate_opencollective(self, page):
        url = 'https://opencollective.com/opencollective1/donate'
        link: Tag = page.find('a', attrs=dict(href=url))
        assert link

        assert 'opencollective.com' in link.select_one('img')['src']

    def test_donate_tidelift(self, page):
        link: Tag = page.find('a', attrs=dict(href='tidelift_url1'))
        assert link

        assert 'Tidelift Subscription' in link.text

    def test_navigation(self, page):
        toctree: Tag = page.select_one('ul.current')
        assert toctree

        # Should have two top-level items in it
        nodes = toctree.find_all('li')
        assert 3 == len(nodes)

        # First
        assert ['toctree-l1'] == nodes[0]['class']
        assert '../hellopage.html' == nodes[0].find('a')['href']
        assert 'Hello Page' == nodes[0].find('a').text

        # Second
        assert ['toctree-l1', 'current'] == nodes[1]['class']
        assert 'index.html' == nodes[1].find('a')['href']
        assert 'Subdir' == nodes[1].find('a').text

        # Third
        assert ['toctree-l2', 'current'] == nodes[2]['class']
        assert '#' == nodes[2].find('a')['href']
        assert 'Subfile' == nodes[2].find('a').text

    def test_extra_nav_links(self, page):
        extra: Tag = page.find('a', attrs=dict(href='extra1'))
        assert 'Extra' == extra.text

    def test_relations_heading(self, page):
        # Relations is display: none but let's test it anyway
        relations: Tag = page.select_one('div.relations')
        assert 'Related Topics' == relations.find('h3').text

        # Entries
        entries = relations.find_all('a')
        assert '../index.html' == entries[0]['href']
        assert 'Documentation overview' == entries[0].text
        assert 'index.html' == entries[1]['href']
        assert 'Subdir' == entries[1].text
        assert 'index.html' == entries[2]['href']
        assert 'Subdir' == entries[2].text
