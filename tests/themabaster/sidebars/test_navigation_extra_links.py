from typing import Tuple

import pytest

from themester.storytime import Story
from themester.themabaster.sidebars.navigation import extra_links


@pytest.mark.parametrize('component_package', (extra_links,))
def test_stories(these_stories: Tuple[Story, ...]):
    story0 = these_stories[0]
    assert None is story0.instance.extra_nav_links
    assert None is story0.instance.resolved_links
    assert None is story0.vdom

    story1 = these_stories[1]
    assert 2 == len(story1.instance.resolved_links)
    assert 'hr' == story1.vdom[0].tag
    assert 'ul' == story1.vdom[1].tag
    li = story1.vdom[1].children[0]
    assert 2 == len(li)
    first_a = li[0].children[0]
    assert 'link1.com' == first_a.props['href']
    assert 'First Link' == first_a.children[0]

    story2 = these_stories[2]
    assert '' is str(story2.html)
