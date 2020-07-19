"""
Relbar2 is a block in the Document component.

This block contains the relation bar, the list of related links
(the parent documents on the left, and the links to
index, modules etc. on the right). Relbar1 appears before
the document, Relbar2 after the document. By default,
both blocks are filled; to show the relbar only.
"""

from dataclasses import dataclass

from viewdom import html, VDOM
from viewdom_wired import component


@component()
@dataclass(frozen=True)
class Relbar2:
    """ Relation bar usually at the bottom. """

    def __call__(self) -> VDOM:
        return html('')
