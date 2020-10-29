from typing import Tuple

from viewdom import html

from themester.nullster.components.hello_world import HelloWorld
from themester.storytime import Story


def all_stories() -> Tuple[Story, ...]:
    story0 = Story(
        component=HelloWorld,
        props=dict(name='Nullster', title='Story Site'),
    )
    story1 = Story(
        component=HelloWorld,
        usage=html('<{HelloWorld} name="Nullster" />')
    )

    return story0, story1
