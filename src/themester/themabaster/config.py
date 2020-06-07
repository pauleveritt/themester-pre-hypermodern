"""

An implementation of the protocol for all the knobs for this layout.

In Sphinx, this would be an instance that was left in the ``conf.py``
file then injected into the site container as a singleton.
"""

from dataclasses import dataclass
from typing import Optional, Iterable

from .protocols import CSSFile, LayoutConfig


@dataclass
class ThemabasterConfig(LayoutConfig):
    lang: str = 'EN'
    site_name: Optional[str] = None
    css_files: Iterable[CSSFile] = tuple()
    file_suffix: str = '.html'
    baseurl: Optional[str] = None