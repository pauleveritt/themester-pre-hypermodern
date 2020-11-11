from typing import Tuple

from viewdom import html

from themester.sphinx.models import Link
from . import RellinkMarkup
from themester.storytime import Story


def all_stories() -> Tuple[Story, ...]:
    story0 = Story(
        component=RellinkMarkup,
        props=dict(
            previous=Link(
                title='Previous',
                link='/previous/',
            ),
            next=Link(
                title='Next',
                link='/next/',
            )
        ),
    )
    story1 = Story(
        component=RellinkMarkup,
        usage=html('<{RellinkMarkup} />')
    )

    return story0, story1
