"""
Relbar2 is a block in the Document component.

This block contains the relation bar, the list of related links
(the parent documents on the left, and the links to
index, modules etc. on the right). Relbar1 appears before
the document, Relbar2 after the document. By default,
both blocks are filled; to show the relbar only.
"""

from dataclasses import dataclass, field

from viewdom import html, VDOM
from viewdom_wired import component
from wired_injector.operators import Get

from ...components.rellink_markup import RellinkMarkup
from ....protocols import ThemeConfig

try:
    from typing import Annotated
except ImportError:
    from typing_extensions import Annotated


@component()
@dataclass
class Relbar2:
    """ Relation bar usually at the bottom. """

    show_relbar_bottom: Annotated[bool, Get(ThemeConfig, attr='show_relbar_top')]
    show_relbars: Annotated[bool, Get(ThemeConfig, attr='show_relbar_top')]
    show_relbar_top: bool = field(init=False)

    def __post_init__(self):
        self.show_relbar_top = self.show_relbar_bottom or self.show_relbars

    def __call__(self) -> VDOM:
        return html('''\n
<div class="related top"><{RellinkMarkup} /> </div>        
        ''') if self.show_relbar_top else []
