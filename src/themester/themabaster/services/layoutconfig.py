"""

An implementation of the protocol for all the knobs for this layout.

In Sphinx, this would be an instance that was left in the ``conf.py``
file then injected into the site container as a singleton.
"""

from dataclasses import dataclass
from typing import Optional

from themester.themabaster.protocols import PropsFiles


# TODO Post-1.0: Make a Protocol for this
@dataclass
class ThemabasterConfig:
    doctype: str = 'html'
    lang: str = 'EN'
    site_name: Optional[str] = None
    css_files: PropsFiles = tuple()
    js_files: PropsFiles = tuple()
    file_suffix: str = '.html'
    baseurl: Optional[str] = None
    favicon: Optional[str] = None
