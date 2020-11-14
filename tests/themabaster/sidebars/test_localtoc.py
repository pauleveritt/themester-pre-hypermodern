from typing import Tuple

import pytest

from themester.storytime import Story
from themester.themabaster.sidebars import localtoc


@pytest.mark.parametrize('component_package', (localtoc,))
def test_stories(these_stories: Tuple[Story, ...]):
    story0 = these_stories[0]
    assert '../mock/index' == story0.instance.resolved_pathto
    assert 'h3' == story0.vdom[0].tag
    assert 'a' == story0.vdom[0].children[0].tag
    assert '../mock/index' == story0.vdom[0].children[0].props['href']
    assert ['Table of Contents'] == story0.vdom[0].children[0].children
    assert '<li>toc</li>' == str(story0.vdom[1])

    story1 = these_stories[1]
    assert [] == story1.vdom

    story2 = these_stories[2]
    expected = '<h3><a href="../mock/index">Table of Contents</a></h3><li>toc</li>'
    assert expected == str(story2.html)
