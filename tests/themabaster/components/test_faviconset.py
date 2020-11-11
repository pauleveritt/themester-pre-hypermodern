from typing import Tuple

import pytest

from themester.storytime import Story
from themester.themabaster.components import faviconset


@pytest.mark.parametrize('component_package', (faviconset,))
def test_stories(these_stories: Tuple[Story, ...]):
    story0 = these_stories[0]
    assert '../mock/static/favicon.ico' == story0.instance.shortcut_href
    assert 4 == len(story0.vdom)
    shortcut = story0.vdom[0]
    assert 'link' == shortcut.tag
    assert '../mock/static/favicon.ico' == shortcut.props['href']
    png = story0.vdom[1]
    assert 'link' == png.tag
    assert '../mock/static/apple-touch-icon-precomposed.png' == png.props['href']
    precomposed = story0.vdom[2]
    assert 'link' == precomposed.tag
    assert 'apple-touch-icon-precomposed' == precomposed.props['rel']
    assert '../mock/static/apple-touch-icon-precomposed.png' == precomposed.props['href']
    sizes = list(story0.vdom[3])
    assert 3 == len(sizes)
    assert '../mock/static/apple-touch-icon-144x144-precomposed.png' == sizes[0].props['href']
    assert '../mock/static/apple-touch-icon-114x114-precomposed.png' == sizes[1].props['href']
    links = story0.html.select('link')
    assert 6 == len(links)

    story1 = these_stories[1]
    assert None is story1.vdom[0]

    story2 = these_stories[2]
    assert None is story2.vdom[3]

    story3 = these_stories[3]
    links = story3.html.select('link')
    assert 6 == len(links)
