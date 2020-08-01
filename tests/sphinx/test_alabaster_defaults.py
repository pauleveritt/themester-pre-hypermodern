# import pytest
# from bs4.element import Tag
#
# # The default values for all theme options, knobs, templates, etc.
# # Nothing customized in conf.py or anywhere else.
#
# pytestmark = pytest.mark.sphinx('html', testroot='basic-theme')
#
#
# @pytest.mark.parametrize('page', ['index.html', ], indirect=True)
# class TestAlabasterLayoutDefaults:
#     """ Structures in Alabaster's ``layout.html`` """
#
#     def test_extrahead(self, page):
#         """ Jinja2 variable defined at top of layout """
#
#         # Custom stylesheet
#         custom: Tag = page.find('link', attrs=dict(rel='stylesheet'))
#         assert '_static/goku.css' == custom['href']
#
#         # Mobile icon for iOS, not there unless added in conf file
#         assert not page.find('link', attrs=dict(rel='apple-touch-icon'))
#
#         # Canonical URL, not present unless flag set
#         assert not page.find('link', attrs=dict(rel='canonical'))
#
#         # viewport
#         viewport: Tag = page.find('meta', attrs=dict(name='viewport'))
#         assert 'device' in viewport['content']
#
#     def test_document_block(self, page):
#         """ The basic theme has a block with some logic in it """
#
#         # render_sidebar is Jinja2 var derived from configuration, defaults to false """
#         assert not page.select('div.bodywraper')
#
#         # A div with class and role
#         assert 'main' == page.find('div', attrs={'class': 'body'})['role']
#
#     def test_block_relbar_bottom(self, page):
#         """theme_show_relbar_bottom is not customized thus false"""
#         assert not page.find('div', attrs={'data-testid': 'related bottom'})
#
#     def test_block_relbar_top(self, page):
#         """top is not customized thus false"""
#         assert not page.find('div', attrs={'data-testid': 'related topr'})
#
#     def test_footer(self, page):
#         """ The footer block """
#
#         footer: Tag = page.find('div', attrs={'class': 'footer'})
#         assert footer
#
#         # See if some of the text nodes and children are present and translated
#         assert '©' in footer.contents[0]
#         f = '\n        ©.\n        \n            |\n            Powered by '
#         assert f == footer.contents[0]
#         assert 'http://sphinx-doc.org/' == footer.contents[1]['href']
#         assert 'Sphinx' in footer.contents[1].text
#
#         # Project name and link should be next
#         assert 'https://github.com/pauleveritt/goku' == footer.contents[3]['href']
#         assert 'Goku' in footer.contents[3].text
#
#         # Page source
#         assert '_sources/index.rst.txt' == footer.contents[5]['href']
#         assert 'Page source' == footer.contents[5].text
#
#     def test_footer_github_banner(self, page):
#         """ Display "fork me", off by default """
#
#         assert not page.select_one('a.github')
#
#     def test_footer_analytics(self, page):
#         """ Insert script for Google Analytics, off by default """
#
#         # As a note, I added a class to the <script> to make it findable
#         assert not page.select_one('script.analytics')
#
#
# @pytest.mark.parametrize('css', ['_static/goku.css', ], indirect=True)
# class TestAlabasterCssDefaults:
#
#     def test_css(self, css):
#         """ Various knobs that affect alabaster.css_t """
#
#         assert 'div.relations' in css
