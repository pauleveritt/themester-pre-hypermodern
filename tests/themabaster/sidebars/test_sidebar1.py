from typing import Tuple

import pytest

from themester.storytime import Story
from themester.themabaster.sidebars import sidebar1


@pytest.mark.parametrize('component_package', (sidebar1,))
def test_stories(these_stories: Tuple[Story, ...]):
    story0 = these_stories[0]
    assert [] == story0.vdom

    story1 = these_stories[1]
    assert '' == str(story1.html)
