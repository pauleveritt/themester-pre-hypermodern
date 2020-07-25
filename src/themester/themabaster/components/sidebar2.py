"""
Sidebar2 is a block in the Content component.
"""

from dataclasses import dataclass
from typing import Tuple, Callable

from viewdom import html, VDOM
from viewdom_wired import component
from wired.dataclasses import injected

from themester.themabaster.config import ThemabasterConfig

from ..components.sidebarlogo import SidebarLogo  # noqa: F401


@component()
@dataclass(frozen=True)
class Sidebar2:
    """ A block in content, presumably for right-column """

    sidebars: Tuple[Callable] = injected(ThemabasterConfig, attr='sidebars')

    def __call__(self) -> VDOM:
        if not self.sidebars:
            return html('')
        else:
            sidebars = [html('<{sidebar} />') for sidebar in self.sidebars]
            return html('''\n
<div class="sphinxsidebar" role="navigation" aria-label="main navigation">
    <div class="sphinxsidebarwrapper">
        <{SidebarLogo} />
        {[sidebar for sidebar in sidebars]}
    </div>
</div>
                    ''')
