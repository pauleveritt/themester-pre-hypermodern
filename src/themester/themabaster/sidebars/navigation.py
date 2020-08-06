"""
Sidebar to show the site global table of contents.

Also allow extra links to be added.
"""

from dataclasses import dataclass, field
from typing import Callable, Optional

from markupsafe import Markup
from viewdom import VDOM, html
from viewdom_wired import component
from wired.dataclasses import injected

from themester.sphinx.config import SphinxConfig
from themester.sphinx.models import PageContext
from .navigation_extra_links import NavigationExtraLinks  # noqa: F401
from ..config import ThemabasterConfig


@component()
@dataclass
class Navigation:
    master_doc: str = injected(SphinxConfig, attr='master_doc')
    pathto: Callable[[str], str] = injected(PageContext, attr='pathto')
    sidebar_collapse: bool = injected(ThemabasterConfig, attr='sidebar_collapse')
    sidebar_includehidden: bool = injected(ThemabasterConfig, attr='sidebar_includehidden')
    toctree: Optional[Callable] = injected(PageContext, attr='toctree')
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
