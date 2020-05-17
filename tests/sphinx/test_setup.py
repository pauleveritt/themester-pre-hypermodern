import pytest

pytestmark = pytest.mark.sphinx('html', testroot='setup')


@pytest.mark.parametrize('page', ['index.html', ], indirect=True)
class TestSetupFunction:
    """ Minimum test for a minimum site.

     This site has no views, resources, no anything. It just uses the
     Themester built-in views.

     """

    def test_index(self, page):
        assert 'Hello World' in page
