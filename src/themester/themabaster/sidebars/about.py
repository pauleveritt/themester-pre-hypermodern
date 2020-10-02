from dataclasses import dataclass

from viewdom import html, VDOM
from viewdom_wired import component

from .about_description import AboutDescription
from .about_github_button import AboutGitHubButton
from .about_logo import AboutLogo
from .about_travis_button import AboutTravisButton


@component()
@dataclass
class About:

    def __call__(self) -> VDOM:
        assert (AboutDescription, AboutGitHubButton, AboutLogo,
                AboutTravisButton)
        return html('''\n
<{AboutLogo} />
<{AboutDescription} />
<{AboutGitHubButton} />
<{AboutTravisButton} />
        ''')
