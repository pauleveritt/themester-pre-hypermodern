"""
Relbar1 is a block in the Document component.

This block contains the relation bar, the list of related links
(the parent documents on the left, and the links to
index, modules etc. on the right). Relbar1 appears before
the document, Relbar2 after the document. By default,
both blocks are filled; to show the relbar only.
"""

from dataclasses import dataclass, field

from viewdom import html, VDOM
from viewdom_wired import component
from wired.dataclasses import injected

from themester.themabaster.config import ThemabasterConfig
from ..components.rellink_markup import RellinkMarkup

from wired_injector.operators import Get, Attr

try:
    from typing import Annotated
except ImportError:
    from typing_extensions import Annotated

@component()
@dataclass
class Relbar1:
    """ Relation bar usually at the top. """

    show_relbar_top: Annotated[
        bool,
        Get(ThemabasterConfig),
        Attr('show_relbar_top'),
    ]
    show_relbars: Annotated[
        bool,
        Get(ThemabasterConfig),
        Attr('show_relbar_top'),
    ]
    resolved_show_relbars: bool = field(init=False)

    def __post_init__(self):
        self.resolved_show_relbars = self.show_relbar_top or self.show_relbars

    def __call__(self) -> VDOM:
        assert RellinkMarkup
        return html('''\n
<div class="related top"><{RellinkMarkup} /> </div>        
        ''') if self.resolved_show_relbars else []
