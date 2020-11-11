from typing import Tuple

from viewdom import html

from . import Title
from themester.storytime import Story


def all_stories() -> Tuple[Story, ...]:
    story0 = Story(
        component=Title,
        props=dict(resource_title='Themabaster', site_title='Story Site'),
    )
    story1 = Story(
        component=Title,
        props=dict(resource_title='<h1>Some Page</h1>', site_title=None),
    )
    story2 = Story(
        component=Title,
        props=dict(resource_title='Themabaster', site_title='Story Site'),
    )
    story3 = Story(
        component=Title,
        usage=html('<{Title} site_title="XYZ" />')
    )

    return story0, story1, story2, story3
