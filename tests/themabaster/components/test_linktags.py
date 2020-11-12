from typing import Tuple

import pytest

from themester.storytime import Story
from themester.themabaster.components import linktags


@pytest.mark.parametrize('component_package', (linktags,))
def test_stories(these_stories: Tuple[Story, ...]):
    story0 = these_stories[0]
    assert 2 == len(story0.instance.resolved_links)
    assert '../mock/genindex' == story0.instance.resolved_links[0]['href']
    assert '../mock/genindex' == story0.vdom[0].props['href']
    assert 'index' == story0.vdom[0].props['rel']
    assert 'Index' == story0.vdom[0].props['title']
    assert '../mock/copyright' == story0.vdom[1].props['href']
    assert 'copyright' == story0.vdom[1].props['rel']
    assert 'Copyright' == story0.vdom[1].props['title']

    story1 = these_stories[1]
    links = story1.html.select('link')
    assert 4 == len(links)
    assert '../mock/about' == links[0].attrs['href']
    assert '../mock/genindex' == links[1].attrs['href']
    assert '../mock/search' == links[2].attrs['href']
    assert '../mock/copyright' == links[3].attrs['href']
