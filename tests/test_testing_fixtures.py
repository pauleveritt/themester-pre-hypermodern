"""

Themester has fixtures for testing, those fixtures need tests.

"""

pytest_plugins = [
    'themester.testing.fixtures',
]


def test_this_container(this_container):
    from themester.sphinx.models import PageContext
    pagecontext: PageContext = this_container.get(PageContext)
    assert 'Some Page' == pagecontext.title
