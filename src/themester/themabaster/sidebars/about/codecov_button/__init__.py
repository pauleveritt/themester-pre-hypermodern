"""
AboutTravisButton is a block in the Sidebar component.
"""

from dataclasses import dataclass, field
from typing import Optional

from viewdom import html, VDOM
from viewdom_wired import component
from wired_injector.operators import Get

from themester.protocols import ThemeConfig

try:
    from typing import Annotated
except ImportError:
    from typing_extensions import Annotated


@component()
@dataclass
class AboutCodeCovButton:
    """ The travis button block in the About sidebar """

    github_repo: Annotated[Optional[str], Get(ThemeConfig, attr='github_repo')]
    github_user: Annotated[Optional[str], Get(ThemeConfig, attr='github_user')]
    codecov_button: Annotated[bool, Get(ThemeConfig, attr='codecov_button')]
    codecov_path: Annotated[str, Get(ThemeConfig, attr='codecov_path')]
    badge_branch: Annotated[str, Get(ThemeConfig, attr='badge_branch')]
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
