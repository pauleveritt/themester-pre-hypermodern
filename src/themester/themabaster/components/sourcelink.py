"""
Sidebar to show a link to the source of the current document.
"""

from dataclasses import dataclass
from typing import Callable

from viewdom import VDOM, html
from viewdom_wired import component
from wired.dataclasses import injected

from themester.sphinx.config import HTMLConfig
from themester.sphinx.models import PageContext


@component()
@dataclass(frozen=True)
class SourceLink:
    show_sourcelink: bool = injected(HTMLConfig, attr='show_sourcelink')
    has_source: bool = injected(HTMLConfig, attr='has_source')
    sourcename: str = injected(PageContext, attr='sourcename')
    pathto: Callable[[str], str] = injected(PageContext, attr='pathto')

    def __call__(self) -> VDOM:
        if self.show_sourcelink and self.has_source and self.sourcename:
            pt = self.pathto(f'_sources/{self.sourcename}')
            return html('''\n
<div role="note" aria-label="source link" data-testid="sourcelink">
    <h3>This Page</h3>
    <ul class="this-page-menu">
        <li>
            <a href={pt} rel="nofollow">Show Source</a>
        </li>
    </ul>
</div>
            ''')
        return html('')
