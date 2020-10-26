from typing import Tuple

from themester.nullster.components.hello_world import HelloWorld
from themester.nullster.storytime_example import resource, themester_app
from themester.storytime import Story


def all_stories() -> Tuple[Story, ...]:
    story0 = Story(
        resource=resource,
        themester_app=themester_app,
        component=HelloWorld,
        props=dict(name='Nullster', title='Story Site'),
    )

    return story0,
