import dataclasses

import pytest
from bs4 import BeautifulSoup
from viewdom import html
from viewdom_wired import render

from themester.protocols import ThemeConfig
from themester.sphinx.models import Link
from themester.themabaster.components.relbar2 import Relbar2

from typing import Tuple

import pytest

from themester.storytime import Story
from themester.themabaster.components import relbar2
from themester.themabaster.components.rellink_markup import RellinkMarkup


@pytest.mark.parametrize('component_package', (relbar2,))
def test_stories(these_stories: Tuple[Story, ...]):
    story0 = these_stories[0]
    this_component = story0.instance
    assert this_component.show_relbar_top
    this_vdom = story0.vdom
    assert 'div' == this_vdom.tag
    assert 'related top' == this_vdom.props['class']
    assert RellinkMarkup == this_vdom.children[0].tag
    this_html = story0.html
    assert ['related', 'top'] == this_html.select_one('div').get('class')
    links = this_html.select('a')
    assert 2 == len(links)
    assert '/previous/' == links[0].get('href')
    assert 'Previous Document' == links[0].get('title')
    assert 'Previous' == links[0].text
    assert '/next/' == links[1].get('href')
    assert 'Next Document' == links[1].get('title')
    assert 'Next' == links[1].text

    story1 = these_stories[1]
    assert '' == str(story1.html)
