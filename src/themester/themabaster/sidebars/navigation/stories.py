from typing import Tuple

from viewdom import html

from themester.storytime import Story
from . import Navigation
from ...stories import theme_config, sphinx_config, page_context


def all_stories() -> Tuple[Story, ...]:
    story0 = Story(
        component=Navigation,
        props=dict(
            master_doc=sphinx_config.master_doc,
            pathto=page_context.pathto,
            sidebar_collapse=theme_config.sidebar_collapse,
            sidebar_includehidden=theme_config.sidebar_includehidden,
            toctree=page_context.toctree,
        ),
    )
    story1 = Story(
        component=Navigation,
        usage=html('<{Navigation} />')
    )

    return story0, story1
