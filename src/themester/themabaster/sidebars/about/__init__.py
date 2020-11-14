from dataclasses import dataclass

from viewdom import html, VDOM
from viewdom_wired import component

from .description import AboutDescription
from .github_button import AboutGitHubButton
from .logo import AboutLogo
from .travis_button import AboutTravisButton


@component()
@dataclass
class About:

    def __call__(self) -> VDOM:
        return html('''\n
<{AboutLogo} />
<{AboutDescription} />
<{AboutGitHubButton} />
<{AboutTravisButton} />
        ''')
