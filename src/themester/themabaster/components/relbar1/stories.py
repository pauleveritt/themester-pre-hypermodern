from typing import Tuple

from viewdom import html

from themester.storytime import Story
from . import Relbar1
from .. import rellink_markup


def all_stories() -> Tuple[Story, ...]:
    story0 = Story(
        component=Relbar1,
        props=dict(
            show_relbar_top=True,
            show_relbars=True,
        ),
        other_packages=(rellink_markup,)
    )
    story1 = Story(
        component=Relbar1,
        usage=html('<{Relbar1} />')
    )

    return story0, story1
