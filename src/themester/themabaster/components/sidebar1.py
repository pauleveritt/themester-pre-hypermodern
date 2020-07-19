"""
Sidebar1 is a block in the Content component.
"""

from dataclasses import dataclass

from viewdom import html, VDOM
from viewdom_wired import component


@component()
@dataclass(frozen=True)
class Sidebar1:
    """ A block in content, presumably for left-column, empty by default """

    def __call__(self) -> VDOM:
        return html('')
