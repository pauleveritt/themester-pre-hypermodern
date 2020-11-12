from typing import Tuple

import pytest

from themester.storytime import Story
from themester.themabaster.components import header


@pytest.mark.parametrize('component_package', (header,))
def test_stories(these_stories: Tuple[Story, ...]):
    story0 = these_stories[0]
    assert [] == story0.vdom.children
    assert '<span></span>' == str(story0.html)
