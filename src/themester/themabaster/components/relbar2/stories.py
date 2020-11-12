from typing import Tuple

from viewdom import html

from themester.storytime import Story
from . import Relbar2
from .. import rellink_markup


def all_stories() -> Tuple[Story, ...]:
    story0 = Story(
        component=Relbar2,
        props=dict(
            show_relbar_bottom=True,
            show_relbars=True,
        ),
        other_packages=(rellink_markup,)
    )
    story1 = Story(
        component=Relbar2,
        usage=html('<{Relbar2} />')
    )

    return story0, story1
