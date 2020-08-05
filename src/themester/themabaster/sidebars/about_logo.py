"""
AboutLogo is a block in the About component.
"""

from dataclasses import dataclass, field
from typing import Callable, Optional

from viewdom import html, VDOM
from viewdom_wired import component
from wired.dataclasses import injected

from themester.sphinx.config import SphinxConfig, HTMLConfig
from themester.sphinx.models import PageContext


@component()
@dataclass
class AboutLogo:
    """ The logo block in the About sidebar """

    logo: Optional[str] = injected(HTMLConfig, attr='logo')
    master_doc: str = injected(SphinxConfig, attr='master_doc')
    pathto: Callable[[str, Optional[int]], str] = injected(PageContext, attr='pathto')
    resolved_master: str = field(init=False)
    resolved_logo: str = field(init=False)

    def __post_init__(self):
        self.resolved_master = self.pathto(self.master_doc, 0)
        self.resolved_logo = self.pathto(f'_static/{self.logo}', 1) if self.logo else ''

    def __call__(self) -> Optional[VDOM]:
        if self.logo:
            return html('''\n
<p class="logo">
    <a href={self.resolved_master}>
        <img class="logo" src={self.resolved_logo} alt="Logo"/>
    </a>
</p>
                    ''')
        return None
