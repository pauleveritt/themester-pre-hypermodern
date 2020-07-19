"""
The DocumentBody component has the docutils-rendered content.

It matches the "body" block in Sphinx.
"""

from dataclasses import dataclass

from viewdom import html, VDOM
from viewdom_wired import component


@component()
@dataclass(frozen=True)
class DocumentBody:
    """ Contains the rendered content of the current page. """

    def __call__(self) -> VDOM:
        return html('')
