"""
AboutGitHubButton is a block in the Sidebar component.
"""

from dataclasses import dataclass, field
from typing import Optional

from viewdom import html, VDOM
from viewdom_wired import component
from wired_injector.operators import Get

from themester.themabaster.config import ThemabasterConfig

try:
    from typing import Annotated
except ImportError:
    from typing_extensions import Annotated


@component()
@dataclass
class AboutGitHubButton:
    """ The github button block in the About sidebar """

    github_button: Annotated[bool, Get(ThemabasterConfig, attr='github_button')]
    github_count: Annotated[str, Get(ThemabasterConfig, attr='github_count')]
    github_repo: Annotated[Optional[str], Get(ThemabasterConfig, attr='github_repo')]
    github_type: Annotated[str, Get(ThemabasterConfig, attr='github_type')]
    github_user: Annotated[Optional[str], Get(ThemabasterConfig, attr='github_user')]
    show_button: bool = field(init=False)

    def __post_init__(self):
        if self.github_button and self.github_repo and self.github_user:
            self.show_button = True
        else:
            self.show_button = False

    def __call__(self) -> Optional[VDOM]:
        if self.show_button:
            return html('''\n
        <p>
            <iframe src="https://ghbtns.com/github-btn.html?user={self.github_user}&repo={self.github_repo}&type={self.github_type}&count={self.github_count}&size=large&v=2"
                    allowtransparency="true" frameborder="0" scrolling="0" width="200px" height="35px"></iframe>
        </p>            
            ''')
        return None
