"""
Sidebar to show the local table of contents (headings within document.)
"""

from dataclasses import dataclass, field
from typing import Callable

from markupsafe import Markup
from viewdom import VDOM, html
from viewdom_wired import component
from wired.dataclasses import injected
from wired_injector.operators import Get

from themester.sphinx.config import SphinxConfig
from themester.sphinx.models import PageContext

try:
    from typing import Annotated
except ImportError:
    from typing_extensions import Annotated


@component()
@dataclass
class LocalToc:
    display_toc: Annotated[bool, Get(PageContext, attr='display_toc')]
    master_doc: Annotated[str, Get(SphinxConfig, attr='master_doc')]
    pathto: Annotated[Callable[[str], str], Get(PageContext, attr='pathto')]
    toc: Annotated[Markup, Get(PageContext, attr='toc')]
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
