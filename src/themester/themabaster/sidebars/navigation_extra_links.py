"""
Sidebar to show the site global table of contents.

Also allow extra links to be added.
"""

from dataclasses import dataclass, field
from typing import Optional

from viewdom import VDOM, html
from viewdom_wired import component
from wired.dataclasses import injected

from themester.sphinx.models import Links
from themester.themabaster.config import ThemabasterConfig


@component()
@dataclass
class NavigationExtraLinks:
    extra_nav_links: Links = injected(ThemabasterConfig, attr='extra_nav_links')
    resolved_links: Optional[VDOM] = field(init=False)

    def __post_init__(self):
        if self.extra_nav_links:
            self.resolved_links = [html('<li class="toctree-l1"><a href={link.link }>{link.title}</a></li>') for link in self.extra_nav_links]
        else:
                self.resolved_links = None

    def __call__(self) -> Optional[VDOM]:
        if self.extra_nav_links:
            return html('''\n
<hr/>
<ul>
{self.resolved_links}
</ul>
            ''')
        return None
