from typing import Tuple

from viewdom import html

from themester import themabaster
from themester.storytime import Story
from . import Body


def all_stories() -> Tuple[Story, ...]:
    story0 = Story(
        component=Body,
    )

    story1 = Story(
        component=Body,
        plugins=(themabaster,),
        usage=html('<{Body} />')
    )

    return story0, story1
