from typing import Protocol, Optional, Tuple, Mapping, Union, Iterable, Callable

from viewdom import VDOM
from viewdom_wired import Component

# TODO Add support for extra attrs
PropsFile = Union[str, Tuple[str, Mapping]]
PropsFiles = Tuple[PropsFile, ...]


class Favicon(Component, Protocol):
    """ Render the link in the head """

    href: str
    static_url: Callable


class Head(Component, Protocol):
    """ A container for the head element and its children """

    favicon: Optional[str]
    page_title: str
    site_name: Optional[str]
    site_css_files: Iterable[str]
    page_css_files: Iterable[str]
    site_js_files: Iterable[str]
    page_js_files: Iterable[str]
    children: Optional[Tuple[VDOM, ...]]
    charset: str


class HTML(Component, Protocol):
    """ The html element """
    lang: str


class BaseLayout(Component, Protocol):
    """ The layout for sublayouts """

    ...


class CSSFiles(Component, Protocol):
    static_url: Callable
    site_files: PropsFiles
    page_files: Optional[PropsFiles]


class JSFiles(Component, Protocol):
    static_url: Callable
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


class Hasdoc(Protocol):
    """ A callable that does what Sphinx's helper does for hasdoc() """

    def __call__(self, target: str) -> bool:
        """ Determine whether that target path, relative to root, exists """
        ...


class Linktags(Component, Protocol):
    """ Insert <link> tags to related documents if present """

    # The "slot" doesn't have any contract. You can put any VDOM
    # in there.
    pass
