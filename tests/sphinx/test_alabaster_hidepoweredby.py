import pytest
from bs4.element import Tag

pytestmark = pytest.mark.sphinx('html', testroot='alabaster-hidepoweredby')


@pytest.mark.parametrize('page', ['index.html', ], indirect=True)
class TestAlabasterHidePoweredBy:
    """ Ensure that show_copyright=false hides everything """

    def test_footer(self, page):

        footer: Tag = page.find('div', attrs={'class': 'footer'})

        # Make sure some of the children are not present
        assert '©' in footer.contents[0]
        assert 'Powered by' not in footer.contents[0]
