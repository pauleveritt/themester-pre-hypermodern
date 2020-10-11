"""
AboutTravisButton is a block in the Sidebar component.
"""

from dataclasses import dataclass, field
from typing import Optional

from viewdom import html, VDOM
from viewdom_wired import component
from wired.dataclasses import injected
from wired_injector.operators import Get

from themester.protocols import ThemeConfig
from themester.themabaster.config import ThemabasterConfig

try:
    from typing import Annotated
except ImportError:
    from typing_extensions import Annotated


@component()
@dataclass
class AboutTravisButton:
    """ The travis button block in the About sidebar """

    github_repo: Annotated[Optional[str], Get(ThemeConfig, attr='github_repo')]
    github_user: Annotated[Optional[str], Get(ThemeConfig, attr='github_user')]
    travis_button: Annotated[bool, Get(ThemeConfig, attr='travis_button')]
    travis_path: Annotated[Optional[str], Get(ThemeConfig, attr='travis_path')]
    badge_branch: Annotated[str, Get(ThemeConfig, attr='badge_branch')]
    resolved_path: str = field(init=False)

    def __post_init__(self):
        if self.travis_path:
            self.resolved_path = self.travis_path
        else:
            self.resolved_path = f'{self.github_user}/{self.github_repo}'

    def __call__(self) -> Optional[VDOM]:
        path = self.resolved_path
        if self.travis_button:
            return html('''\n
<p>
    <a class="badge" href="https://travis-ci.org/{path}">
        <img
            alt="https://secure.travis-ci.org/{path}.svg?branch={self.badge_branch}"
            src="https://secure.travis-ci.org/{path}.svg?branch={self.badge_branch}"
        />
    </a>
</p>
            ''')
        return None
