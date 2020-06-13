"""

An implementation of the protocol for all the knobs for this layout.

In Sphinx, this would be an instance that was left in the ``conf.py``
file then injected into the site container as a singleton.
"""

from dataclasses import dataclass
from typing import Optional, Iterable, Union, Tuple, Mapping

from themester.themabaster.protocols import LayoutConfig

# TODO Add support for extra attrs
CSSFile = Union[str, Tuple[str, Mapping]]
JSFile = Union[str, Tuple[str, Mapping]]


@dataclass
class ThemabasterConfig(LayoutConfig):
    lang: str = 'EN'
    site_name: Optional[str] = None
    css_files: Iterable[CSSFile] = tuple()
    js_files: Iterable[CSSFile] = tuple()
    file_suffix: str = '.html'
    baseurl: Optional[str] = None
