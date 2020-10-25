from typing import Tuple

from themester import nullster
from themester.nullster.components.hello_world import HelloWorld
from themester.nullster.storytime_example import resource, themester_app
from themester.protocols import Resource
from themester.storytime import Story

services = ((resource, Resource),)


def all_stories() -> Tuple[Story, ...]:
    story0 = Story(
        themester_app=themester_app,
        package=nullster,
        component=HelloWorld,
        props=dict(name='Nullster', title='Story Site'),
        services=services,
    )

    return story0,
