import dataclasses

import pytest
from bs4 import BeautifulSoup
from viewdom import html
from viewdom_wired import render

from themester.protocols import ThemeConfig
from themester.sphinx import SphinxConfig
from themester.themabaster.config import ThemabasterConfig
from themester.themabaster.sidebars.donate import Donate

from typing import Tuple

import pytest

from themester.storytime import Story
from themester.themabaster.sidebars import donate


@pytest.mark.parametrize('component_package', (donate,))
def test_stories(these_stories: Tuple[Story, ...]):
    story0 = these_stories[0]
    assert not story0.instance.show_donate

    story1 = these_stories[1]
    assert story1.instance.show_donate

    story2 = these_stories[2]
    assert '' == str(story2.html)

    story3 = these_stories[3]
    h3 = story3.html.select_one('h3').text
    assert 'Donate/support' == h3
    badges = story3.html.select('a')
    assert 'donate.com' == badges[0].get('href')
    assert 'https://opencollective.com/opencollective.com/donate' == badges[1].get('href')
    assert 'tidelift.com' == badges[2].get('href')
