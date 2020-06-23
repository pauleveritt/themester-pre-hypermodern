from typing import Protocol, Optional, Tuple, Iterable, Mapping, Union

from viewdom_wired import Component

from themester import Resource

# CSSFile = Union[str, Tuple[str, Mapping]]
# JSFile = Union[str, Tuple[str, Mapping]]

# TODO Add support for extra attrs
PropsFile = Union[str, Tuple[str, Mapping]]
PropsFiles = Tuple[PropsFile, ...]


class Head(Component, Protocol):
    """ A container for the head element and its children """
    page_title: str


class CSSFiles(Component, Protocol):
    resource: Resource
    site_files: PropsFiles
    page_files: Optional[PropsFiles]


class JSFiles(Component, Protocol):
    resource: Resource
    site_files: Tuple[str, ...]
    page_files: Optional[Tuple[str, ...]]


class Layout(Component, Protocol):
    """ All the contracts for any theme implementing this layout """
    site_name: str


class LayoutConfig(Protocol):
    """ Configuration options used in this layout """

    baseurl: Optional[str]
    css_files: PropsFiles
    doctype: str
    file_suffix: str
    js_files: PropsFiles
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
