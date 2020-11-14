from typing import Tuple

import pytest

from themester.storytime import Story
from themester.themabaster.sidebars import navigation


@pytest.mark.parametrize('component_package', (navigation,))
def test_stories(these_stories: Tuple[Story, ...]):
    story0 = these_stories[0]
    assert '../mock/index' == story0.instance.resolved_pathto
    assert '<ul><li>First</li></ul>' == str(story0.instance.resolved_toctree)
    assert 'div' == story0.vdom.tag
    assert 'h3' == story0.vdom.children[0].tag
    assert 'a' == story0.vdom.children[0].children[0].tag
    assert '../mock/index' == story0.vdom.children[0].children[0].props['href']
    assert ['Table of Contents'] == story0.vdom.children[0].children[0].children

    story1 = these_stories[1]
    assert '../mock/index' == story1.html.select_one('a').attrs['href']
    assert 'First' == story1.html.select_one('li').text
