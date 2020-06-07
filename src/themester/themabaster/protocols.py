from __future__ import annotations

from typing import Protocol, Optional, Union, Tuple, Mapping

from viewdom import VDOM
from viewdom_wired import Children

# TODO Add support for extra attrs
CSSFile = Union[str, Tuple[str, Mapping]]
JSFile = Union[str, Tuple[str, Mapping]]


class HTML(Protocol):
    """ The html element """
    lang: str
    head: Head


class Component(Protocol):
    def __call__(self) -> VDOM:
        ...


class Title(Component, Protocol):
    """ A configurable title element with policies """

    page_title: str
    site_name: str


class Head(Protocol):
    """ A container for the head element and its children """
    children: Children


class LayoutConfig(Protocol):
    """ Configuration options used in this layout """
    doctype: str
    lang: str
    site_name: Optional[str]
    file_suffix: str
    baseurl: Optional[str]


class Layout(Protocol):
    """ All the contracts for any theme implementing this layout """
    site_name: str
