from typing import Tuple

from viewdom import html

from themester.storytime import Story
from themester.themabaster.stories import theme_config
from . import AboutCodeCovButton


def all_stories() -> Tuple[Story, ...]:
    story0 = Story(
        component=AboutCodeCovButton,
        props=dict(
            codecov_button=theme_config.codecov_button,
            codecov_path=theme_config.codecov_path,
            github_repo=theme_config.github_repo,
            github_user=theme_config.github_user,
            badge_branch=theme_config.badge_branch,
        ),
    )

    story1 = Story(
        component=AboutCodeCovButton,
        props=dict(
            codecov_button=True,
            codecov_path=theme_config.codecov_path,
            github_repo='thisrepo',
            github_user='thisuser',
            badge_branch=theme_config.badge_branch,
        ),
    )

    story2 = Story(
        component=AboutCodeCovButton,
        usage=html('<{AboutCodeCovButton} />')
    )

    return story0, story1, story2
