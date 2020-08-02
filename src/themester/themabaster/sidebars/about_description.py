"""
SidebarLogo is a block in the Sidebar component.
"""

from dataclasses import dataclass
from typing import Optional

from viewdom import html, VDOM
from viewdom_wired import component
from wired.dataclasses import injected

from themester.themabaster.config import ThemabasterConfig


@component()
@dataclass
class AboutDescription:
    """ The description block in the About sidebar """

    description: Optional[str] = injected(ThemabasterConfig, attr='description')

    def __call__(self) -> Optional[VDOM]:
        if self.description:
            return html('<p class="blurb">{self.description}</p>')
        return None
