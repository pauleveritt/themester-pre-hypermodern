from typing import Tuple

from viewdom import html

from themester.sphinx.models import Link
from themester.storytime import Story
from . import NavigationExtraLinks
from ....stories import theme_config


def all_stories() -> Tuple[Story, ...]:
    story0 = Story(
        component=NavigationExtraLinks,
        props=dict(
            extra_nav_links=theme_config.extra_nav_links,
        ),
    )
    story1 = Story(
        component=NavigationExtraLinks,
        props=dict(
            extra_nav_links=(
                Link(title='First Link', link='link1.com'),
                Link(title='Second Link', link='link2.com'),
            )
        ),
    )
    story2 = Story(
        component=NavigationExtraLinks,
        usage=html('<{NavigationExtraLinks} />')
    )

    return story0, story1, story2
