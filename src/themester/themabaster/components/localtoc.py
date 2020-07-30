"""
Sidebar to show the local table of contents (headings within document.)
"""

from dataclasses import dataclass, field
from typing import Callable

from markupsafe import Markup
from viewdom import VDOM, html
from viewdom_wired import component
from wired.dataclasses import injected

from themester.sphinx.config import SphinxConfig
from themester.sphinx.models import PageContext


@component()
@dataclass
class LocalToc:
    display_toc: bool = injected(PageContext, attr='display_toc')
    master_doc: str = injected(SphinxConfig, attr='master_doc')
    pathto: Callable[[str], str] = injected(PageContext, attr='pathto')
    toc: Markup = injected(PageContext, attr='toc')
    resolved_pathto: str = field(init=False)

    def __post_init__(self):
        self.resolved_pathto = self.pathto(self.master_doc)

    def __call__(self) -> VDOM:
        if self.display_toc:
            return html('''\n
<h3><a href={self.resolved_pathto}>Table of Contents</a></h3>
{self.toc}
            ''')
        return html('')
