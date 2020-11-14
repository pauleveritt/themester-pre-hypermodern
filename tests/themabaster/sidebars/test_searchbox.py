from typing import Tuple

import pytest

from themester.storytime import Story
from themester.themabaster.sidebars import searchbox


@pytest.mark.parametrize('component_package', (searchbox,))
def test_stories(these_stories: Tuple[Story, ...]):
    story0 = these_stories[0]
    assert '../mock/search' == story0.instance.resolved_pathto
    assert 'div' == story0.vdom[0].tag
    assert '../mock/search' == story0.vdom[0].children[1].children[0].props['action']

    story1 = these_stories[1]
    assert '../mock/search' == story1.html.select_one('form').attrs['action']
