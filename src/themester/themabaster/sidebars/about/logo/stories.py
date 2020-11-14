from typing import Tuple

from viewdom import html

from themester.storytime import Story
from themester.themabaster.stories import sphinx_config, page_context
from . import AboutLogo


def all_stories() -> Tuple[Story, ...]:
    story0 = Story(
        component=AboutLogo,
        props=dict(
            logo='site_logo.png',
            master_doc=sphinx_config.master_doc,
            pathto=page_context.pathto,
        ),
    )
    story1 = Story(
        component=AboutLogo,
        props=dict(
            logo=None,
            master_doc=sphinx_config.master_doc,
            pathto=page_context.pathto,
        ),
    )
    story2 = Story(
        component=AboutLogo,
        usage=html('<{AboutLogo} logo="site_logo.png" />')
    )

    return story0, story1, story2
