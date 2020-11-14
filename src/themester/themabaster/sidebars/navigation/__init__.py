"""
Sidebar to show the site global table of contents.

Also allow extra links to be added.
"""

from dataclasses import dataclass, field
from typing import Callable, Optional

from markupsafe import Markup
from viewdom import VDOM, html
from viewdom_wired import component
from wired_injector.operators import Get

from themester.sphinx.config import SphinxConfig
from themester.sphinx.models import PageContext
from .extra_links import NavigationExtraLinks
from ....protocols import ThemeConfig

try:
    from typing import Annotated
except ImportError:
    from typing_extensions import Annotated


@component()
@dataclass
class Navigation:
    master_doc: Annotated[str, Get(SphinxConfig, attr='master_doc')]
    pathto: Annotated[Callable[[str], str], Get(PageContext, attr='pathto')]
    sidebar_collapse: Annotated[bool, Get(ThemeConfig, attr='sidebar_collapse')]
    sidebar_includehidden: Annotated[bool, Get(ThemeConfig, attr='sidebar_includehidden')]
    toctree: Annotated[Optional[Callable], Get(PageContext, attr='toctree')]
    resolved_pathto: str = field(init=False)
    resolved_toctree: Markup = field(init=False)

    def __post_init__(self):
        self.resolved_pathto = self.pathto(self.master_doc)
        self.resolved_toctree = Markup(
            self.toctree(
                sidebar_collapse=self.sidebar_collapse,
                sidebar_includehidden=self.sidebar_includehidden,
            ))

    def __call__(self) -> VDOM:
        return html('''\n
<div>
    <h3><a href={self.resolved_pathto}>Table of Contents</a></h3>
    {self.resolved_toctree}
    <{NavigationExtraLinks} />
</div>
        ''')
