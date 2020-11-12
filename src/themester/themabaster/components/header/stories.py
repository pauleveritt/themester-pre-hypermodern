from typing import Tuple

from viewdom import html

from themester.storytime import Story
from . import Header


def all_stories() -> Tuple[Story, ...]:
    story0 = Story(
        component=Header,
        props=dict(),
    )
    story1 = Story(
        component=Header,
        usage=html('<{Header} />')
    )

    return story0, story1
