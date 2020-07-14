from typing import Protocol, Optional, Tuple, Mapping, Union

# TODO Add support for extra attrs
PropsFile = Union[str, Tuple[str, Mapping]]
PropsFiles = Tuple[PropsFile, ...]


class LayoutConfig(Protocol):
    """ Configuration options used in this layout """

    baseurl: Optional[str]
    css_files: PropsFiles
    doctype: str
    file_suffix: str
    js_files: PropsFiles
    lang: str
    site_name: Optional[str]


class Hasdoc(Protocol):
    """ A callable that does what Sphinx's helper does for hasdoc() """

    def __call__(self, target: str) -> bool:
        """ Determine whether that target path, relative to root, exists """
        ...
