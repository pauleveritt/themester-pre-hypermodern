"""

An implementation of the protocol for all the knobs for this layout.

In Sphinx, this would be an instance that was left in the ``conf.py``
file then injected into the site container as a singleton.
"""

from dataclasses import dataclass, field
from typing import Optional, Tuple, Callable

from themester.utils import PropsFiles


def get_sidebars():
    """ Escape circular import hell """

    from .components.globaltoc import GlobalToc  # noqa: F401
    from .components.localtoc import LocalToc  # noqa: F401
    from .components.relations import Relations  # noqa: F401
    from .components.searchbox import SearchBox  # noqa: F401
    from .components.sourcelink import SourceLink  # noqa: F401
    return (
        LocalToc,
        GlobalToc,
        Relations,
        SourceLink,
        SearchBox,
    )


@dataclass(frozen=True)
class ThemabasterConfig:
    # Sphinx Config


    # Sphinx Template Context Globals
    copyright: Optional[str] = None
    favicon: Optional[str] = None
    file_suffix: str = '.html'
    has_source: bool = True
    language: str = 'EN'
    logo: Optional[str] = None
    master_doc: str = 'index'
    show_source: bool = True


    # HTML Theme
    baseurl: Optional[str] = None
    css_files: PropsFiles = tuple()
    js_files: PropsFiles = tuple()
    show_copyright: bool = True
    sidebars: Tuple[Callable, ...] = field(default_factory=get_sidebars)

    # Custom/Other
    doctype: str = 'html'
    no_sidebar: bool = False
    show_powered_by: bool = True
    show_relbar_bottom: bool = False
    show_relbar_top: bool = False
    show_relbars: bool = False
    site_name: Optional[str] = None
    touch_icon: Optional[str] = None
