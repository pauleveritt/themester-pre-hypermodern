"""
Sidebar to show related topics previous/next/parents.
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
class Relations:
    master_doc: str = injected(SphinxConfig, attr='master_doc')
    pathto: Callable[[str], str] = injected(PageContext, attr='pathto')
    toctree: Optional[Callable[[], str]] = injected(PageContext, attr='toctree')
    resolved_pathto: str = field(init=False)
    resolved_toctree: Markup = field(init=False)

    def __post_init__(self):
        self.resolved_pathto = self.pathto(self.master_doc)
        self.resolved_toctree = Markup(self.toctree())

    def __call__(self) -> VDOM:
        # Alabaster has a weird relations.html which isn't really well-formed
        # on looping. This makes it not-well-formed on snippets.
        #
        # TODO Let's skip relations.html for now, not sure it is used.
        return html('''\n
<div class="relations">
    <h3>Related Topics</h3>
    <ul>
        <li><a href={self.resolved_pathto}>Documentation overview</a>
        </li>
    </ul>
    <p><strong>UNIMPLEMENTED</strong></p>
</div>
        ''')
