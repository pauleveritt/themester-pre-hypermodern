from typing import Protocol, Optional, Tuple, Mapping, Union

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


class HTML(Component, Protocol):
    """ The html element """
    lang: str


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


class Title(Component, Protocol):
    page_title: str
    site_name: Optional[str]
