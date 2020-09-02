from typing import Tuple

import pytest

from themester.nullster.components import hello_world
from themester.storytime import Story


@pytest.mark.parametrize('component_package', (hello_world,))
def test_stories(these_stories: Tuple[Story, ...]):
    story0 = these_stories[0]
    assert 'Nullster' == story0.instance.name
