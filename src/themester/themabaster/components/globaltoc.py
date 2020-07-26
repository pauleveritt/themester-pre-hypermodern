"""
Sidebar to show the site global table of contents.
"""

from dataclasses import dataclass
from typing import Callable, Optional

from markupsafe import Markup
from viewdom import VDOM, html
from viewdom_wired import component
from wired.dataclasses import injected

from themester.sphinx import PageContext, SphinxConfig


@component()
@dataclass(frozen=True)
class GlobalToc:
    master_doc: str = injected(SphinxConfig, attr='master_doc')
    pathto: Callable[[str], str] = injected(PageContext, attr='pathto')
    toctree: Optional[Callable[[], str]] = injected(PageContext, attr='toctree')

    def __call__(self) -> VDOM:
        this_toctree = Markup(self.toctree())
        pt = self.pathto(self.master_doc)
        return html('''\n
<div>
    <h3><a href={pt}>Table of Contents</a></h3>
    {this_toctree}
</div>
        ''')
