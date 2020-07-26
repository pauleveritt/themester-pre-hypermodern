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
    master_doc: str = 'index'

    # HTML Builder
    baseurl: Optional[str] = None
    copy_source: bool = True
    css_files: PropsFiles = tuple()
    favicon: Optional[str] = None
    file_suffix: str = '.html'
    js_files: PropsFiles = tuple()
    show_copyright: bool = True
    show_sourcelink: bool = True
    sidebars: Tuple[Callable, ...] = field(default_factory=get_sidebars)

    # HTML Templating Global Variables
    has_source: bool = True
    logo: Optional[str] = None

    # Sphinx Basic
    nosidebar: bool = False

    # Alabaster
    show_powered_by: bool = True
    show_relbar_bottom: bool = False
    show_relbar_top: bool = False
    show_relbars: bool = False
    touch_icon: Optional[str] = None

    # Custom/Other
    doctype: str = 'html'
