"""
AboutLogo is a block in the About component.
"""

from dataclasses import dataclass, field
from typing import Callable, Optional

from viewdom import html, VDOM
from viewdom_wired import component
from wired.dataclasses import injected
from wired_injector.operators import Get

from themester.sphinx.config import SphinxConfig, HTMLConfig
from themester.sphinx.models import PageContext

try:
    from typing import Annotated
except ImportError:
    from typing_extensions import Annotated


@component()
@dataclass
class AboutLogo:
    """ The logo block in the About sidebar """

    logo: Annotated[Optional[str], Get(HTMLConfig, attr='logo')]
    master_doc: Annotated[str, Get(SphinxConfig, attr='master_doc')]
    pathto: Annotated[Callable[[str, Optional[int]], str], Get(PageContext, attr='pathto')]
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
