from typing import Tuple

from themester import nullster
from themester.nullster.components.hello_world import HelloWorld
from themester.storytime import Story


def all_stories() -> Tuple[Story, ...]:
    story0 = Story(
        package=nullster,
        component=HelloWorld,
        props=dict(name='Nullster'),
    )

    return story0,
