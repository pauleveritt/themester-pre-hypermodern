"""
A block in the body, above the content block.
"""

from dataclasses import dataclass

from viewdom import VDOM, html
from viewdom_wired import component


@component()
@dataclass(frozen=True)
class Header:
    """ A block in the body above the content block, empty by default. """

    def __call__(self) -> VDOM:
        return html('<span></span>')
