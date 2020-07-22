"""
Generate markup for a top/bottom rellink block.

Alabaster has blocks which you can put in the content
block to show the rellinks, either at top or bottom.
These are off by default. Both blocks are driven by
a macro named ``rellink_markup``.

This component expects to be passed an optional previous
and/or next, each having link and title attributes.
"""

from dataclasses import dataclass

from viewdom import html, VDOM
from viewdom_wired import component

from ..services.prevnext import PreviousLink, NextLink


@component()
@dataclass(frozen=True)
class RellinkMarkup:
    """ Markup for rellink bars. """

    previous: PreviousLink
    next: NextLink

    def __call__(self) -> VDOM:
        prev = html('''\n
<li>
    &larr;
    <a href="{self.previous.link}" title="Previous Document">{self.previous.title}</a>
</li>
''') if self.previous else None
        n = html('''\n
<li>
    <a href="{self.next.link}" title="Next Document">{self.next.title}</a>
    &rarr;
</li>
''') if self.previous else None
        return html('''\n
<nav id="rellinks">
    <ul>
        {prev}
        {n}
    </ul>
</nav>       
        ''')
