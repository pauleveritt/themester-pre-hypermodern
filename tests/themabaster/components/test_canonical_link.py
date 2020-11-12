from typing import Tuple

import pytest

from themester.storytime import Story
from themester.themabaster.components import canonical_link


@pytest.mark.parametrize('component_package', (canonical_link,))
def test_stories(these_stories: Tuple[Story, ...]):
    story0 = these_stories[0]
    assert 'https://somewhere.com/mysite/somedoc.html' == story0.instance.canonical_href
    assert 'canonical' == story0.vdom.props['rel']
    link = story0.html.select_one('link')
    assert 'canonical' == link.get('rel')[0]
    assert 'https://somewhere.com/mysite/somedoc.html' == link.get('href')

    story1 = these_stories[1]
    expected = 'https://somewhere.com/mysite/somedoc.html'
    assert None is story1.instance.canonical_href
    assert None is story1.vdom

    story2 = these_stories[2]
    link = story2.html.select_one('link')
    assert 'canonical' == link.get('rel')[0]
    assert 'https://somewhere.com/mysite/somedoc.html' == link.get('href')
