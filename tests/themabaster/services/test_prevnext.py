from themester.themabaster.services.prevnext import PreviousLink, NextLink


def test_prevnextlinks():
    """ Barely useful, just ensure the API """
    pl = PreviousLink(title='Previous', link='/p/')
    assert 'Previous' == pl.title
    nl = NextLink(title='Next', link='/p/')
    assert 'Next' == nl.title
