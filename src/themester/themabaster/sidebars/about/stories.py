from typing import Tuple

from viewdom import html

from themester.storytime import Story
from . import About


def all_stories() -> Tuple[Story, ...]:
    story0 = Story(
        component=About,
    )
    story1 = Story(
        component=About,
        usage=html('<{About} />')
    )

    return story0, story1
