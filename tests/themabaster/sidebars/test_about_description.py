from typing import Tuple

import pytest

from themester.storytime import Story
from themester.themabaster.sidebars.about import description


@pytest.mark.parametrize('component_package', (description,))
def test_stories(these_stories: Tuple[Story, ...]):
    story0 = these_stories[0]
    assert None is story0.instance.description
    assert None is story0.vdom

    story1 = these_stories[1]
    assert 'p' == story1.vdom.tag
    assert 'Some Project' == story1.vdom.children[0]

    story2 = these_stories[2]
    assert '' == str(story2.html)
