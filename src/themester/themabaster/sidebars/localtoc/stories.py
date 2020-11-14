from typing import Tuple

from viewdom import html

from themester.storytime import Story
from . import LocalToc
from ...stories import page_context, sphinx_config


def all_stories() -> Tuple[Story, ...]:
    story0 = Story(
        component=LocalToc,
        props=dict(
            display_toc=page_context.display_toc,
            master_doc=sphinx_config.master_doc,
            pathto=page_context.pathto,
            toc=page_context.toc,
        ),
    )
    story1 = Story(
        component=LocalToc,
        props=dict(
            display_toc=False,
            master_doc=sphinx_config.master_doc,
            pathto=page_context.pathto,
            toc=page_context.toc,
        ),
    )
    story2 = Story(
        component=LocalToc,
        usage=html('<{LocalToc} />')
    )

    return story0, story1, story2
