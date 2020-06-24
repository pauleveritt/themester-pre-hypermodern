"""
Information from the underlying system about the current page.

In general we want to rely on a resource tree for data about the
currently-rendering "page". But in some systems, like Sphinx, the
framework provides some important computation.

This service collects all the data that themabaster needs -- i.e.
the contract -- for the current "page context".
"""

from dataclasses import dataclass
from typing import Iterable, Any, Tuple, Optional, Dict, Callable


@dataclass(frozen=True)
class Rellink:
    pagename: str
    link_text: str
    title: Optional[str] = None
    accesskey: Optional[str] = None


Rellinks = Optional[Tuple[Rellink, ...]]


@dataclass(frozen=True)
class Link:
    """ A connection to another resource """

    link: str
    title: str


Links = Optional[Tuple[Link, ...]]
Meta = Optional[Dict[str, Dict[str, Any]]]

"""
<a href="{{ pathto(rellink[0])|e }}" title="{{ rellink[1]|striptags|e }}"
             {{ accesskey(rellink[2]) }}>{{ rellink[3] }}</a>
"""


# TODO Post-1.0: Make a Protocol for this
@dataclass(frozen=True)
class PageContext:
    """ Per-page info from the underlying system needed for by layout """

    title: str
    body: str
    sourcename: Optional[str]
    toc: str
    display_toc: bool
    page_source_suffix: str
    css_files: Iterable[str]
    js_files: Iterable[str]
    meta: Meta = None
    metatags: str = ''
    next: Links = None
    parents: Links = None
    prev: Links = None
    rellinks: Rellinks = None
    toctree: Optional[Callable] = None
