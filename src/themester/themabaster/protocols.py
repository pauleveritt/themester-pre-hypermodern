from __future__ import annotations

from typing import Protocol, Optional

from viewdom_wired import Children


class HTML(Protocol):
    """ The html element """
    lang: str
    head: Head


class Title(Protocol):
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


class Layout(Protocol):
    """ All the contracts for any theme implementing this layout """
    site_name: str
