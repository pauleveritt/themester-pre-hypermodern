"""
Sidebar to show the local table of contents (headings within document.)
"""

from dataclasses import dataclass
from typing import Callable

from markupsafe import Markup
from viewdom import VDOM, html
from viewdom_wired import component
from wired.dataclasses import injected

from themester.sphinx import PageContext, SphinxConfig


@component()
@dataclass(frozen=True)
class LocalToc:
    display_toc: bool = injected(PageContext, attr='display_toc')
    master_doc: str = injected(SphinxConfig, attr='master_doc')
    pathto: Callable[[str], str] = injected(PageContext, attr='pathto')
    toc: Markup = injected(PageContext, attr='toc')

    def __call__(self) -> VDOM:
        if self.display_toc:
            pt = self.pathto(self.master_doc)
            return html('''\n
<h3><a href={pt}>Table of Contents</a></h3>
{self.toc}
            ''')
        return html('')
