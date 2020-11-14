from typing import Tuple

import pytest
from bs4 import Doctype

from themester.storytime import Story
from themester.themabaster.components import base_layout


def doctype(soup):
    items = [item for item in soup.contents if isinstance(item, Doctype)]
    return items[0] if items else None


@pytest.mark.parametrize('component_package', (base_layout,))
def test_stories(these_stories: Tuple[Story, ...]):
    story0 = these_stories[0]
    assert dict(lang='EN') == story0.instance.html_props

    story1 = these_stories[1]
    assert 'EN' == story1.html.select_one('html').get('lang')
    assert 17 == len(story1.html.select('html head link'))
    assert 'html' == doctype(story1.html)

    story2 = these_stories[2]
    assert 'html5' == doctype(story2.html)
