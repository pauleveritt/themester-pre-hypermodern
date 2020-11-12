from typing import Tuple

from viewdom import html

from themester.storytime import Story
from . import Head
from .. import title, cssfiles, canonical_link, faviconset, jsfiles, linktags
from ...stories import fake_pathto

extrahead = html('''\n
<link rel="first"/>
<link rel="second"/>
    ''')


def all_stories() -> Tuple[Story, ...]:
    story0 = Story(
        component=Head,
        props=dict(
            extrahead=None,
            pathto=fake_pathto,
        )
    )

    story1 = Story(
        component=Head,
        props=dict(
            extrahead=extrahead,
            pathto=fake_pathto,
        )
    )

    story2 = Story(
        component=Head,
        scannables=(
            canonical_link,
            cssfiles,
            faviconset,
            jsfiles,
            linktags,
            title,
        ),
        usage=html('<{Head} />')
    )

    return story0, story1, story2
