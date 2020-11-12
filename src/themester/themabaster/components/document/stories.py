from typing import Tuple

from markupsafe import Markup
from viewdom import html

from themester.storytime import Story
from . import Document
from .. import relbar1, relbar2


def all_stories() -> Tuple[Story, ...]:
    story0 = Story(
        component=Document,
        props=dict(
            body=Markup('<p>Some content</p>'),
            nosidebar=False,
        ),
    )

    story1 = Story(
        component=Document,
        other_packages=(relbar1, relbar2,),
        usage=html('<{Document} />')
    )

    return story0, story1
