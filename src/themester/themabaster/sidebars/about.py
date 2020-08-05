from dataclasses import dataclass

from viewdom import html, VDOM
from viewdom_wired import component

from .about_description import AboutDescription  # noqa: F401
from .about_github_button import AboutGitHubButton  # noqa: F401
from .about_logo import AboutLogo  # noqa: F401
from .about_travis_button import AboutTravisButton  # noqa: F401


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
