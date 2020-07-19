"""
A block in the body, below the content block.
"""

from dataclasses import dataclass

from viewdom import VDOM, html
from viewdom_wired import component


@component()
@dataclass(frozen=True)
class Footer:
    """ A block in the body below the content block. """

    def __call__(self) -> VDOM:
        return html('')
