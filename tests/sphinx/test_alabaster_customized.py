# import bs4
# import pytest
# from bs4.element import Tag
#
# # The default values for all theme options, knobs, templates, etc.
# # Nothing customized in conf.py or anywhere else.
#
# pytestmark = pytest.mark.sphinx('html', testroot='alabaster-customized')
#
#
# @pytest.mark.parametrize('page', ['subdir/subfile.html', ], indirect=True)
# class TestAlabasterCustomizedConf:
#     """ Twiddle a bunch of knobs in the conf file """
#
#     def test_touch_icon(self, page):
#         icon: Tag = page.find('link', attrs=dict(rel='apple-touch-icon'))
#         assert '../_static/touch_icon1' == icon['href']
#
#     def test_canonical_url(self, page):
#         link: Tag = page.find('link', attrs=dict(rel='canonical'))
#         assert 'canonical_url1subdir/subfile.html' == link['href']
#
#     def test_footer_github_banner(self, page):
#         """ Display "fork me", off by default """
#
#         github: Tag = page.select_one('a.github')
#         assert 'https://github.com/github_user1/github_repo1' == github['href']
#
#     def test_analytics_id(self, page):
#         analytics_id: Tag = page.find(attrs={'data-testid': 'theme_analytics_id'})
#         assert 'analytics_id1' in analytics_id.text
#
#     def test_relbar_bottom(self, page):
#         """theme_show_relbar_bottom is True, jumps into macro rellink_markup"""
#
#         relbar_bottom: Tag = page.find('div', attrs={'data-testid': 'theme_relbar_bottom'})
#         assert relbar_bottom
#
#         assert 1 == len(relbar_bottom.find_all('a'))
#         first_link: Tag = relbar_bottom.find('a')
#         assert 'index.html' == first_link['href']
#         assert 'Previous document' == first_link['title']
#         assert 'Subdir' == first_link.text
#
#     def test_relbar_top(self, page):
#         """show_relbar_top is True, jumps into macro rellink_markup"""
#
#         relbar_top: Tag = page.find('div', attrs={'data-testid': 'theme_relbar_top'})
#         assert relbar_top
#
#         assert 1 == len(relbar_top.find_all('a'))
#         this_link: Tag = relbar_top.find('a')
#         assert 'Subdir' == this_link.text
#         assert 'Previous document' == this_link['title']
#         assert 'index.html' == this_link['href']
#
#     def test_language(self, page):
#         """ Adding this to global conf affects the <html> """
#
#         node: Tag = page.select_one('html')
#         assert 'fr' == node.get('lang')
#
#     def test_encoding(self, page):
#         """ The meta charset is driven by a flag with a default to not display  """
#
#         node: Tag = page.find('meta', attrs={'charset': 'ascii'})
#         assert node
#
#
# @pytest.mark.parametrize('page', ['subdir/subfile.html', ], indirect=True)
# class TestAlabasterCustomizedBlocks:
#     """ Use a custom layout.html template to fill some blocks in the contract """
#
#     def test_doctype(self, page):
#         doctype = [item for item in page.contents if isinstance(item, bs4.Doctype)][0]
#         assert 'html' == doctype
#
#     def test_extrahead(self, page):
#         extrahead: Tag = page.find(attrs={'data-testid': 'extrahead'})
#         assert 'http://author1' == extrahead['href']
#
#     def test_relbar1(self, page):
#         # In refactoring we removed this, as Alabaster was
#         # filling it wth nothingness.
#         relbar1: Tag = page.find(attrs={'data-testid': 'block-relbar1'})
#         assert not relbar1
#
#     def test_relbar2(self, page):
#         # In refactoring we removed this, as Alabaster was
#         # filling it wth nothingness.
#         relbar2: Tag = page.find(attrs={'data-testid': 'block-relbar2'})
#         assert not relbar2
#
#     def test_content(self, page):
#         content: Tag = page.find(attrs={'data-testid': 'block-content'})
#         assert 'content1' == content.text
#
#     def test_footer(self, page):
#         footer: Tag = page.find(attrs={'data-testid': 'block-footer'})
#         assert 'footer1' == footer.text
