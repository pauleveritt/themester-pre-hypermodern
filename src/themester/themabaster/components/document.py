"""
Docuemnt is a block in the Content component.
"""

from dataclasses import dataclass

from viewdom import html, VDOM
from viewdom_wired import component


@component()
@dataclass(frozen=True)
class Document:
    """ A block in content, holding most of the info on this resource """

    def __call__(self) -> VDOM:
        return html('')
