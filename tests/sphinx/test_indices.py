# """
#
# Test the optional sidebars in the basic theme as well as the modindex
# and other generated pages.
#
# """
# import pytest
# from bs4.element import Tag
#
# pytestmark = pytest.mark.sphinx('html', testroot='indices')
#
# @pytest.mark.xfail
# @pytest.mark.parametrize('page', ['genindex.html', ], indirect=True)
# class TestBasicGenindex:
#     """ Turn on the optional html_sidebars in the basic theme """
#
#     def test_heading(self, page):
#         heading: Tag = page.select_one('h1#index')
#         assert heading
#
#         # The href on the link
#         assert 'Index' == heading.text
