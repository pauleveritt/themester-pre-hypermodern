from typing import Tuple

from viewdom import html

from themester.storytime import Story
from . import SearchBox
from ...stories import page_context


def all_stories() -> Tuple[Story, ...]:
    story0 = Story(
        component=SearchBox,
        props=dict(
            builder=page_context.builder,
            pagename=page_context.pagename,
            pathto=page_context.pathto,
        ),
    )
    story1 = Story(
        component=SearchBox,
        usage=html('<{SearchBox} />')
    )

    return story0, story1
