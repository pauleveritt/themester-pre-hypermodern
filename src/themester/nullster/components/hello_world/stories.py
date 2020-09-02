from typing import Tuple

from themester.nullster.components import hello_world
from themester.nullster.components.hello_world import HelloWorld
from themester.storytime import Story


def all_stories() -> Tuple[Story, ...]:
    story0 = Story(
        package=hello_world,
        component=HelloWorld,
        props=dict(name='Nullster'),
    )

    return story0,
