"""
Sidebar2 is a block in the Content component.
"""

from dataclasses import dataclass

from viewdom import html, VDOM
from viewdom_wired import component
from wired.dataclasses import injected

from themester.themabaster.services.layoutconfig import ThemabasterConfig


@component()
@dataclass(frozen=True)
class Sidebar2:
    """ A block in content, presumably for right-column """

    no_sidebar: bool = injected(ThemabasterConfig, attr='no_sidebar')

    def __call__(self) -> VDOM:
        if self.no_sidebar:
            return html('')
        else:
            return html('''\n
<div class="sphinxsidebar" role="navigation" aria-label="main navigation">
    <div class="sphinxsidebarwrapper">
    </div>
</div>
                    ''')
