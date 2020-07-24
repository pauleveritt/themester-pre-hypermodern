"""

An implementation of the protocol for all the knobs for this layout.

In Sphinx, this would be an instance that was left in the ``conf.py``
file then injected into the site container as a singleton.
"""

from dataclasses import dataclass
from typing import Optional

from themester.themabaster.protocols import PropsFiles


@dataclass(frozen=True)
class ThemabasterConfig:
    logo: Optional[str] = None
    baseurl: Optional[str] = None
    css_files: PropsFiles = tuple()
    doctype: str = 'html'
    favicon: Optional[str] = None
    file_suffix: str = '.html'
    has_source: bool = True
    js_files: PropsFiles = tuple()
    lang: str = 'EN'
    master_doc: str = 'index'
    no_sidebar: bool = False
    show_relbar_bottom: bool = False
    show_relbar_top: bool = False
    show_relbars: bool = False
    show_source: bool = True
    site_name: Optional[str] = None
    touch_icon: Optional[str] = None
