"""
AboutTravisButton is a block in the Sidebar component.
"""

from dataclasses import dataclass, field
from typing import Optional

from viewdom import html, VDOM
from viewdom_wired import component
from wired.dataclasses import injected

from themester.themabaster.config import ThemabasterConfig


@component()
@dataclass
class AboutCodeCovButton:
    """ The travis button block in the About sidebar """

    github_repo: Optional[str] = injected(ThemabasterConfig, attr='github_repo')
    github_user: Optional[str] = injected(ThemabasterConfig, attr='github_user')
    codecov_button: bool = injected(ThemabasterConfig, attr='codecov_button')
    codecov_path: Optional[str] = injected(ThemabasterConfig, attr='codecov_path')
    badge_branch: str = injected(ThemabasterConfig, attr='badge_branch')
    resolved_path: str = field(init=False)

    def __post_init__(self):
        if self.codecov_path:
            self.resolved_path = self.codecov_path
        else:
            self.resolved_path = f'{self.github_user}/{self.github_repo}'

    def __call__(self) -> Optional[VDOM]:
        path = self.resolved_path
        if self.codecov_button:
            return html('''\n
<p>
    <a class="badge" href="https://codecov.io/github/{path}">
        <img
                alt="https://codecov.io/github/{path}/coverage.svg?branch={self.badge_branch}"
                src="https://codecov.io/github/{path}/coverage.svg?branch={self.badge_branch}"
        />
    </a>
</p>
            ''')
        return None
