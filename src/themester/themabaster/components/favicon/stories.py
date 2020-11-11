from typing import Tuple

from viewdom import html

from . import Favicon
from themester.storytime import Story



def all_stories() -> Tuple[Story, ...]:
    story0 = Story(
        component=Favicon,
        props=dict(href='someicon.png'),
    )
    story1 = Story(
        component=Favicon,
        usage=html('<{Favicon} />')
    )

    return story0, story1
