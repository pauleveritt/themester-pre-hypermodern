from typing import Tuple

from viewdom import html

from themester.storytime import Story
from . import CSSFiles
from ...stories import html_config, theme_config, page_context


def all_stories() -> Tuple[Story, ...]:
    story0 = Story(
        component=CSSFiles,
        props=dict(
            site_files=html_config.css_files,
            theme_files=theme_config.css_files,
            page_files=page_context.css_files,
        ),
    )
    story1 = Story(
        component=CSSFiles,
        usage=html('<{CSSFiles} />')
    )

    return story0, story1
