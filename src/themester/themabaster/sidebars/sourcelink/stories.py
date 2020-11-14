from typing import Tuple

from viewdom import html

from themester.storytime import Story
from . import SourceLink
from ...stories import page_context


def all_stories() -> Tuple[Story, ...]:
    story0 = Story(
        component=SourceLink,
        props=dict(
            show_sourcelink=True,
            has_source=True,
            pathto=page_context.pathto,
            sourcename='thispage.md',
        ),
    )
    story1 = Story(
        component=SourceLink,
        usage=html('<{SourceLink} />')
    )

    return story0, story1
