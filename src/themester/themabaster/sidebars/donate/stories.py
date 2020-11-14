from typing import Tuple

from viewdom import html

from themester.storytime import Story
from . import Donate
from ...stories import theme_config, sphinx_config


def all_stories() -> Tuple[Story, ...]:
    story0 = Story(
        component=Donate,
        props=dict(
            donate_url=theme_config.donate_url,
            opencollective=theme_config.opencollective,
            opencollective_button_color=theme_config.opencollective_button_color,
            project=sphinx_config.project,
            tidelift_url=theme_config.tidelift_url,
        ),
    )
    story1 = Story(
        component=Donate,
        props=dict(
            donate_url='someurl',
            opencollective=theme_config.opencollective,
            opencollective_button_color=theme_config.opencollective_button_color,
            project=sphinx_config.project,
            tidelift_url=theme_config.tidelift_url,
        ),
    )
    story2 = Story(
        component=Donate,
        usage=html('<{Donate} />')
    )
    story3 = Story(
        component=Donate,
        usage=html(
            '<{Donate} donate_url="donate.com" opencollective="opencollective.com" tidelift_url="tidelift.com"  />')
    )

    return story0, story1, story2, story3
