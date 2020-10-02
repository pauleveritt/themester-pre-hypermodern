"""
Sidebar to show a link to the source of the current document.
"""

from dataclasses import dataclass, field
from typing import Callable

from viewdom import VDOM, html
from viewdom_wired import component
from wired.dataclasses import injected
from wired_injector.operators import Get

from themester.sphinx.config import HTMLConfig
from themester.sphinx.models import PageContext

try:
    from typing import Annotated
except ImportError:
    from typing_extensions import Annotated


@component()
@dataclass
class SourceLink:
    show_sourcelink: Annotated[bool, Get(HTMLConfig, attr='show_sourcelink')]
    has_source: Annotated[bool, Get(HTMLConfig, attr='has_source')]
    sourcename: Annotated[str, Get(PageContext, attr='sourcename')]
    pathto: Annotated[Callable[[str], str], Get(PageContext, attr='pathto')]
    resolved_pathto: str = field(init=False)

    def __post_init__(self):
        self.resolved_pathto = self.pathto(f'_sources/{self.sourcename}')

    def __call__(self) -> VDOM:
        if self.show_sourcelink and self.has_source and self.sourcename:
            return html('''\n
<div role="note" aria-label="source link" data-testid="sourcelink">
    <h3>This Page</h3>
    <ul class="this-page-menu">
        <li>
            <a href={self.resolved_pathto} rel="nofollow">Show Source</a>
        </li>
    </ul>
</div>
            ''')
        return html('')
