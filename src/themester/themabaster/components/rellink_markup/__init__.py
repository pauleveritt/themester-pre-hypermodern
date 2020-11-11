"""
Generate markup for a top/bottom rellink block.

Alabaster has blocks which you can put in the content
block to show the rellinks, either at top or bottom.
These are off by default. Both blocks are driven by
a macro named ``rellink_markup``.

This component expects to be passed an optional previous
and/or next, each having link and title attributes.
"""

from dataclasses import dataclass, field

from viewdom import html, VDOM
from viewdom_wired import component
from wired_injector.operators import Get, Attr

from themester.sphinx.models import Link, PageContext

try:
    from typing import Annotated
except ImportError:
    from typing_extensions import Annotated


@component()
@dataclass
class RellinkMarkup:
    """ Markup for rellink bars. """

    previous: Annotated[
        Link,
        Get(PageContext),
        Attr('prev'),
    ]
    next: Annotated[
        Link,
        Get(PageContext),
        Attr('next'),
    ]
    resolved_previous: VDOM = field(init=False)
    resolved_next: VDOM = field(init=False)

    def __post_init__(self):
        self.resolved_previous = html('''\n
<li>
    &larr;
    <a href="{self.previous.link}" title="Previous Document">{self.previous.title}</a>
</li>
''') if self.previous else None
        self.resolved_next = html('''\n
<li>
    <a href="{self.next.link}" title="Next Document">{self.next.title}</a>
    &rarr;
</li>
''') if self.previous else None

    def __call__(self) -> VDOM:
        return html('''\n
<nav id="rellinks">
    <ul>
        {self.resolved_previous}
        {self.resolved_next}
    </ul>
</nav>       
        ''')
