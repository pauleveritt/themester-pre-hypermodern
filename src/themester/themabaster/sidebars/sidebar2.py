"""
Sidebar2 is a block in the Content component.
"""

from dataclasses import dataclass, field
from typing import Tuple, Callable

from viewdom import html, VDOM
from viewdom_wired import component
from wired.dataclasses import injected

from themester.themabaster.config import ThemabasterConfig
from themester.themabaster.sidebars.about_logo import AboutLogo  # noqa: F401


@component()
@dataclass
class Sidebar2:
    """ A block in content, presumably for right-column """

    sidebars: Tuple[Callable] = injected(ThemabasterConfig, attr='sidebars')
    resolved_sidebars: VDOM = field(init=False)

    def __post_init__(self):
        self.resolved_sidebars = [html('<{sidebar} />') for sidebar in self.sidebars]

    def __call__(self) -> VDOM:
        if not self.sidebars:
            return html('')
        else:
            return html('''\n
<div class="sphinxsidebar" role="navigation" aria-label="main navigation">
    <div class="sphinxsidebarwrapper">
        {[sidebar for sidebar in self.resolved_sidebars]}
    </div>
</div>
                    ''')
