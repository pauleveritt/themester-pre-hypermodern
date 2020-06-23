from typing import Protocol, Optional, Tuple, Iterable, Mapping, Union

from viewdom import VDOM
from viewdom_wired import Component


class CSSFiles(Component, Protocol):
    site_files = Tuple[str, ...]
    page_files = Optional[Tuple[str, ...]]


class Head(Component, Protocol):
    """ A container for the head element and its children """
    children: VDOM


class JSFiles(Component, Protocol):
    site_files = Tuple[str, ...]
    page_files = Optional[Tuple[str, ...]]


class Layout(Component, Protocol):
    """ All the contracts for any theme implementing this layout """
    site_name: str


# TODO Add support for extra attrs
CSSFile = Union[str, Tuple[str, Mapping]]
JSFile = Union[str, Tuple[str, Mapping]]


class LayoutConfig(Protocol):
    """ Configuration options used in this layout """

    baseurl: Optional[str]
    css_files: Iterable[CSSFile]
    doctype: str
    file_suffix: str
    js_files: Iterable[JSFile]
    lang: str
    site_name: Optional[str]


class PageContext:
    """ Per-page info from the underlying system needed for by layout """

    body: str
    css_files: Iterable[str]
    js_files: Iterable[str]
    page_title: str
    prev: Optional[Mapping[str, str]]
    next: Optional[Mapping[str, str]]


class Title(Component, Protocol):
    page_title: str
    site_name: Optional[str]

# from __future__ import annotations
#
# from typing import Protocol, Optional, Union, Tuple, Mapping
#
# class HTML(Protocol):
#     """ The html element """
#     lang: str
#     # head: Head
#
#
# class LayoutConfig(Protocol):
#     """ Configuration options used in this layout """
#     doctype: str
#     lang: str
#     site_name: Optional[str]
#     file_suffix: str
#     baseurl: Optional[str]
#
#
# class Layout(Protocol):
#     """ All the contracts for any theme implementing this layout """
#     site_name: str
