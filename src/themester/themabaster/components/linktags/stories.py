from typing import Tuple

from viewdom import html

from themester.storytime import Story
from . import Linktags, SemanticLink
from ...stories import fake_hasdoc, fake_pathto

link1: SemanticLink = dict(
    rel='index',
    docname='genindex',
    title='Index'
)
link2: SemanticLink = dict(
    rel='author',
    docname='author',
    title='Author'
)
link3: SemanticLink = dict(
    rel='copyright',
    docname='copyright',
    title='Copyright'
)
links = (link1, link2, link3)


def all_stories() -> Tuple[Story, ...]:
    story0 = Story(
        component=Linktags,
        props=dict(
            hasdoc=fake_hasdoc,
            pathto=fake_pathto,
            links=links,
        ),
    )
    story1 = Story(
        component=Linktags,
        usage=html('<{Linktags} />')
    )

    return story0, story1
