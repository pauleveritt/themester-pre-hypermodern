from typing import Tuple

from viewdom import html

from themester.storytime import Story
from . import Content
from .. import relbar1


def all_stories() -> Tuple[Story, ...]:
    story0 = Story(
        component=Content,
    )

    story1 = Story(
        component=Content,
        scannables=(relbar1,),
        usage=html(f'<{Content} />')
    )

    return story0, story1
