from typing import Tuple

from viewdom import html

from themester.storytime import Story
from . import Sidebar1


def all_stories() -> Tuple[Story, ...]:
    story0 = Story(
        component=Sidebar1,
        props=dict(
        ),
    )
    story1 = Story(
        component=Sidebar1,
        usage=html('<{Sidebar1} />')
    )

    return story0, story1
