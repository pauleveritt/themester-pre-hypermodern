from typing import Tuple

import pytest

from themester.storytime import Story
from themester.themabaster.sidebars import sourcelink
from typing import Tuple

import pytest

from themester.storytime import Story
from themester.themabaster.sidebars import sourcelink


@pytest.mark.parametrize('component_package', (sourcelink,))
def test_stories(these_stories: Tuple[Story, ...]):
    story0 = these_stories[0]
    assert '../mock/_sources/thispage.md' == story0.instance.resolved_pathto
    assert 'div' == story0.vdom.tag
    a = story0.vdom.children[1].children[0].children[0]
    assert 'a' == a.tag
    assert '../mock/_sources/thispage.md' == a.props['href']

    story1 = these_stories[1]
    assert '<div' in str(story1.html)
