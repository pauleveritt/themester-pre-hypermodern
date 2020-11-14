import pytest
from viewdom import html
from viewdom_wired import render

from themester.sphinx import SphinxConfig
from themester.themabaster.sidebars.relations import Relations

from typing import Tuple

import pytest

from themester.storytime import Story
from themester.themabaster.sidebars import relations


@pytest.mark.parametrize('component_package', (relations,))
def test_stories(these_stories: Tuple[Story, ...]):
    story0 = these_stories[0]
    assert '../mock/index' == story0.instance.resolved_pathto
    assert '<ul><li>First</li></ul>' == str(story0.instance.resolved_toctree)
    assert 'div' == story0.vdom.tag
    assert 'h3' == story0.vdom.children[0].tag
    ul = story0.vdom.children[1]
    assert 'ul' == ul.tag
    assert 'li' == ul.children[0].tag
    first_li = ul.children[0]
    assert 'li' == first_li.tag
    assert 'a' == first_li.children[0].tag
    assert '../mock/index' == first_li.children[0].props['href']
    assert ['Documentation overview'] == first_li.children[0].children

    story1 = these_stories[1]
    assert 'relations' == story1.html.select_one('div').attrs['class'][0]
