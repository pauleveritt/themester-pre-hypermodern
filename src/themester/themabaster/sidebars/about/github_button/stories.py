from typing import Tuple

from viewdom import html

from themester.storytime import Story
from themester.themabaster.stories import theme_config
from . import AboutGitHubButton


def all_stories() -> Tuple[Story, ...]:
    story0 = Story(
        component=AboutGitHubButton,
        props=dict(
            github_button=theme_config.github_button,
            github_repo=theme_config.github_repo,
            github_user=theme_config.github_user,
            github_type=theme_config.github_type,
            github_count=theme_config.github_count,
        ),
    )
    story1 = Story(
        component=AboutGitHubButton,
        props=dict(
            github_button=True,
            github_repo='repo',
            github_user='user',
            github_count='true',
            github_type='watch',
        ),
    )
    story2 = Story(
        component=AboutGitHubButton,
        usage=html('<{AboutGitHubButton} />')
    )

    story3 = Story(
        component=AboutGitHubButton,
        usage=html(
            '<{AboutGitHubButton} github_button={True} github_repo="thisrepo" github_user="thisuser" /> ')
    )

    return story0, story1, story2, story3
