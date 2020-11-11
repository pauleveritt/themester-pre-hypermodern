import dataclasses
from typing import Tuple

from viewdom import html

from themester.storytime import Story
from . import FaviconSet
from ...stories import theme_config
from ...storytime_example import fake_pathto

no_shortcut = dataclasses.replace(theme_config.favicons)
no_shortcut.shortcut = None
no_sizes = dataclasses.replace(theme_config.favicons)
no_sizes.sizes = None


def all_stories() -> Tuple[Story, ...]:
    story0 = Story(
        component=FaviconSet,
        props=dict(
            favicons=dataclasses.replace(theme_config.favicons),
            pathto=fake_pathto,
        ),
    )
    story1 = Story(
        component=FaviconSet,
        props=dict(
            favicons=no_shortcut,
            pathto=fake_pathto,
        ),
    )
    story2 = Story(
        component=FaviconSet,
        props=dict(
            favicons=no_sizes,
            pathto=fake_pathto,
        ),
    )
    story3 = Story(
        component=FaviconSet,
        usage=html('<{FaviconSet} />')
    )

    return story0, story1, story2, story3
