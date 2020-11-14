from typing import Tuple

from viewdom import html

from themester.storytime import Story
from . import Relations
from ...stories import sphinx_config, page_context


def all_stories() -> Tuple[Story, ...]:
    story0 = Story(
        component=Relations,
        props=dict(
            master_doc=sphinx_config.master_doc,
            pathto=page_context.pathto,
            toctree=page_context.toctree,
        ),
    )
    story1 = Story(
        component=Relations,
        usage=html('<{Relations} />')
    )

    return story0, story1
