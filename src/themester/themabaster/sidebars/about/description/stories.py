from typing import Tuple

from viewdom import html

from themester.storytime import Story
from themester.themabaster.stories import theme_config
from . import AboutDescription


def all_stories() -> Tuple[Story, ...]:
    story0 = Story(
        component=AboutDescription,
        props=dict(
            description=theme_config.description
        ),
    )
    story1 = Story(
        component=AboutDescription,
        props=dict(
            description='Some Project'
        ),
        usage=html('<{AboutDescription} />')
    )
    story2 = Story(
        component=AboutDescription,
        usage=html('<{AboutDescription} />')
    )

    return story0, story1, story2
