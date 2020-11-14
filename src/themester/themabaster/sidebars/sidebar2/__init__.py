"""
Sidebar2 is a block in the Content component.
"""

from dataclasses import dataclass, field
from typing import Tuple

from viewdom import html, VDOM
from viewdom_wired import component, Component
from wired_injector.operators import Get

from themester.protocols import ThemeConfig

try:
    from typing import Annotated
except ImportError:
    from typing_extensions import Annotated


@component()
@dataclass
class Sidebar2:
    """ A block in content, presumably for right-column """

    sidebars: Annotated[
        Tuple[Component],
        Get(ThemeConfig, attr='sidebars'),
    ]
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
