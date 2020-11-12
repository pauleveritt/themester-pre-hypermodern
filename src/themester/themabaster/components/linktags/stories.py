from typing import Tuple

from viewdom import html

from themester.storytime import Story
from . import Linktags
from ...stories import html_config, theme_config, page_context, fake_hasdoc, fake_pathto


def all_stories() -> Tuple[Story, ...]:
    story0 = Story(
        component=Linktags,
        props=dict(
            hasdoc=fake_hasdoc,
            pathto=fake_pathto,
        ),
    )
    story1 = Story(
        component=Linktags,
        usage=html('<{Linktags} />')
    )

    return story0, story1
