"""
Sidebar to show a link to the source of the current document.
"""

from dataclasses import dataclass, field
from typing import Callable

from viewdom import VDOM, html
from viewdom_wired import component
from wired.dataclasses import injected

from themester.sphinx.config import HTMLConfig
from themester.sphinx.models import PageContext


@component()
@dataclass
class SourceLink:
    show_sourcelink: bool = injected(HTMLConfig, attr='show_sourcelink')
    has_source: bool = injected(HTMLConfig, attr='has_source')
    sourcename: str = injected(PageContext, attr='sourcename')
    pathto: Callable[[str], str] = injected(PageContext, attr='pathto')
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
