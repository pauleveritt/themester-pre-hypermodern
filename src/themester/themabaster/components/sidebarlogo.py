"""
SidebarLogo is a block in the Sidebar component.
"""

from dataclasses import dataclass
from typing import Callable, Optional

from viewdom import html, VDOM
from viewdom_wired import component
from wired.dataclasses import injected

from themester.sphinx import PageContext, SphinxConfig, HTMLConfig


@component()
@dataclass(frozen=True)
class SidebarLogo:
    """ The logo in the Sidebar block component """

    logo: str = injected(HTMLConfig, attr='logo')
    master_doc: str = injected(SphinxConfig, attr='master_doc')
    pathto: Callable[[str, Optional[int]], str] = injected(PageContext, attr='pathto')

    def __call__(self) -> VDOM:
        if self.logo:
            pt_master = self.pathto(self.master_doc)
            pt_logo = self.pathto(f'_static/{self.logo}', 1)
            return html('''\n
<p class="logo">
    <a href={pt_master}>
        <img class="logo" src={pt_logo} alt="Logo"/>
    </a>
</p>
                    ''')
        return html('')
