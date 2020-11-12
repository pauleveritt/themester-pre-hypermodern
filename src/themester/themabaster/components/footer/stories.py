from typing import Tuple

from viewdom import html

from themester.storytime import Story
from themester.themabaster.stories import fake_pathto
from . import Footer


def all_stories() -> Tuple[Story, ...]:
    story0 = Story(
        component=Footer,
        props=dict(
            copyright='Bazinga',
            has_source=True,
            pathto=fake_pathto,
            show_powered_by=True,
            show_copyright=True,
            show_sourcelink=True,
            sourcename='',
        ),
    )

    story1 = Story(
        component=Footer,
        usage=html('<{Footer} />')
    )

    return story0, story1
