from typing import Tuple

import pytest

from themester.storytime import Story
from themester.themabaster.components import linktags


@pytest.mark.parametrize('component_package', (linktags,))
def test_stories(these_stories: Tuple[Story, ...]):
    story0 = these_stories[0]
    assert '../mock/about' == story0.instance.resolved_links[0]['href']
    assert '../mock/about' == story0.vdom[0].props['href']
    assert '../mock/about' == story0.html.select('link')[0].attrs['href']

    story1 = these_stories[1]
    assert '../mock/about' == story1.html.select('link')[0].attrs['href']
