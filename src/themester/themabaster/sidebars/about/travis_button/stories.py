from typing import Tuple

from viewdom import html

from themester.storytime import Story
from themester.themabaster.stories import theme_config
from . import AboutTravisButton


def all_stories() -> Tuple[Story, ...]:
    story0 = Story(
        component=AboutTravisButton,
        props=dict(
            travis_button=theme_config.travis_button,
            travis_path=theme_config.travis_path,
            github_repo=theme_config.github_repo,
            github_user=theme_config.github_user,
            badge_branch=theme_config.badge_branch,
        ),
    )
    story1 = Story(
        component=AboutTravisButton,
        props=dict(
            travis_button=True,
            travis_path=theme_config.travis_path,
            github_repo='thisrepo',
            github_user='thisuser',
            badge_branch=theme_config.badge_branch,
        ),
    )
    story2 = Story(
        component=AboutTravisButton,
        usage=html('<{AboutTravisButton} />')
    )
    story3 = Story(
        component=AboutTravisButton,
        usage=html('<{AboutTravisButton} travis_button={True} github_repo="thisrepo" github_user="thisuser" />')
    )

    return story0, story1, story2, story3
