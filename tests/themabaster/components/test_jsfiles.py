from typing import Tuple

import pytest

from themester.storytime import Story
from themester.themabaster.components import jsfiles


@pytest.mark.parametrize('component_package', (jsfiles,))
def test_stories(these_stories: Tuple[Story, ...]):
    story0 = these_stories[0]
    assert 2 == len(story0.instance.srcs)
    assert 'page_first.js' == story0.instance.srcs[0]
    srcs = story0.html.select('script')
    assert 2 == len(srcs)
    assert 'page_first.js' == srcs[0].attrs['src']

    story1 = these_stories[1]
    scripts = story1.html.select('script')
    assert 2 == len(scripts)
    assert '../mock/page_first.js' == scripts[0].attrs['src']
