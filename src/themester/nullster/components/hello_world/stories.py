from typing import Tuple

from themester import nullster
from themester.nullster.components.hello_world import HelloWorld
from themester.protocols import Resource
from themester.storytime import Story
from themester.testing.resources import Site

resource = Site(title='Nullster Site')
services = ((resource, Resource),)


def all_stories() -> Tuple[Story, ...]:
    story0 = Story(
        package=nullster,
        component=HelloWorld,
        props=dict(name='Nullster', title='Story Site'),
        services=services,
    )

    return story0,
