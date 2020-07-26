"""
Sidebar to show related topics previous/next/parents.
"""

from dataclasses import dataclass
from typing import Callable, Optional

from markupsafe import Markup
from viewdom import VDOM, html
from viewdom_wired import component
from wired.dataclasses import injected

from themester.sphinx import PageContext, SphinxConfig


@component()
@dataclass(frozen=True)
class Relations:
    master_doc: str = injected(SphinxConfig, attr='master_doc')
    pathto: Callable[[str], str] = injected(PageContext, attr='pathto')
    toctree: Optional[Callable[[], str]] = injected(PageContext, attr='toctree')

    def __call__(self) -> VDOM:
        this_toctree = Markup(self.toctree())
        pt = self.pathto(self.master_doc)

        # Alabaster has a weird relations.html which isn't really well-formed
        # on looping. This makes it not-well-formed on snippets.
        #
        # TODO Let's skip relations.html for now, not sure it is used.
        return html('''\n
<div class="relations">
    <h3>Related Topics</h3>
    <ul>
        <li><a href={pt}>Documentation overview</a>
        </li>
    </ul>
    <p><strong>UNIMPLEMENTED</strong></p>
</div>
        ''')
