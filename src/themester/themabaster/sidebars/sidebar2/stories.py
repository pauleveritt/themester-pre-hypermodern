from typing import Tuple

from viewdom import html

from themester.storytime import Story
from . import Sidebar2
from .. import localtoc, relations, sourcelink, searchbox
from ...stories import theme_config


def all_stories() -> Tuple[Story, ...]:
    story0 = Story(
        component=Sidebar2,
        props=dict(
            sidebars=theme_config.sidebars,
        ),
    )
    story1 = Story(
        component=Sidebar2,
        props=dict(
            sidebars=tuple(),
        ),
    )
    story2 = Story(
        component=Sidebar2,
        scannables=(localtoc, relations, sourcelink, searchbox),
        usage=html('<{Sidebar2} />')
    )

    return story0, story1, story2
