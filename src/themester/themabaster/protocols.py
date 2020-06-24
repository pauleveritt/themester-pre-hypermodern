from typing import Protocol, Optional, Tuple, Mapping, Union, Iterable

from viewdom_wired import Component

from themester import Resource

# TODO Add support for extra attrs
from themester.url import URL

PropsFile = Union[str, Tuple[str, Mapping]]
PropsFiles = Tuple[PropsFile, ...]


class Favicon(Component, Protocol):
    """ Render the link in the head """

    href: str


class Head(Component, Protocol):
    """ A container for the head element and its children """

    favicon: Optional[str]
    page_title: str
    site_name: Optional[str]
    site_css_files: Iterable[str]
    page_css_files: Iterable[str]
    site_js_files: Iterable[str]
    page_js_files: Iterable[str]
    url: URL
    charset: str


class HTML(Component, Protocol):
    """ The html element """
    lang: str


class CSSFiles(Component, Protocol):
    url: URL
    site_files: PropsFiles
    page_files: Optional[PropsFiles]


class JSFiles(Component, Protocol):
    url: URL
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


class Title(Component, Protocol):
    page_title: str
    site_name: Optional[str]
