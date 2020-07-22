"""
Get the rendered markdown/rst of the current page from the container.

Sphinx renders the current page into HTML and makes that available in
the PageContext. The Sphinx "adapter" will, in html_context, take
that and register a singleton, for the below class, in the per-request
container.
"""

from dataclasses import dataclass

from markupsafe import Markup


@dataclass(frozen=True)
class DocumentBody:
    """ Contains the rendered content of the current page. """

    html: Markup
