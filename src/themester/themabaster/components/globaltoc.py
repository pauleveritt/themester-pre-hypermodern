"""
Sidebar to show the site global table of contents.
"""

from dataclasses import dataclass, field
from typing import Callable, Optional

from markupsafe import Markup
from viewdom import VDOM, html
from viewdom_wired import component
from wired.dataclasses import injected

from themester.sphinx.config import SphinxConfig
from themester.sphinx.models import PageContext


@component()
@dataclass
class GlobalToc:
    master_doc: str = injected(SphinxConfig, attr='master_doc')
    pathto: Callable[[str], str] = injected(PageContext, attr='pathto')
    toctree: Optional[Callable[[], str]] = injected(PageContext, attr='toctree')
    resolved_pathto: str = field(init=False)
    resolved_toctree: Markup = field(init=False)

    def __post_init__(self):
        self.resolved_pathto = self.pathto(self.master_doc)
        self.resolved_toctree = Markup(self.toctree())

    def __call__(self) -> VDOM:
        return html('''\n
<div>
    <h3><a href={self.resolved_pathto}>Table of Contents</a></h3>
    {self.resolved_toctree}
</div>
        ''')
