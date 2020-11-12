from typing import Tuple

import pytest

from themester.storytime import Story
from themester.themabaster.components import document


@pytest.mark.parametrize('component_package', (document,))
def test_stories(these_stories: Tuple[Story, ...]):
    story0 = these_stories[0]
    div = story0.vdom.children[0]
    assert 'div' == div.tag

    story1 = these_stories[1]
    assert story1.html.select_one('div.documentwrapper')
