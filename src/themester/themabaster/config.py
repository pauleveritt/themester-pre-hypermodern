"""

An implementation of the protocol for all the knobs for this layout.

In Sphinx, this would be an instance that was left in the ``conf.py``
file then injected into the site container as a singleton.
"""

from dataclasses import dataclass, field
from typing import Optional, Tuple, Callable, Sequence


@dataclass
class FaviconSize:
    size: str
    filename: str


@dataclass
class Favicons:
    """ Configure a potential set of ico/png images at different sizes.

    Presumes images are in the static directory once deployed and are relative to it.
     """

    shortcut: Optional[str] = 'favicon.ico'
    png: Optional[str] = 'apple-touch-icon-precomposed.png'
    sizes: Optional[Sequence[FaviconSize]] = (
        FaviconSize(size='72x72', filename='apple-touch-icon-144x144-precomposed.png'),
        FaviconSize(size='114x114', filename='apple-touch-icon-114x114-precomposed.png'),
        FaviconSize(size='144x144', filename='apple-touch-icon-72x72-precomposed.png'),
    )

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
    # HTML Builder
    sidebars: Tuple[Callable, ...] = field(default_factory=get_sidebars)

    # Alabaster
    description: Optional[str] = None
    show_powered_by: bool = True
    show_relbar_bottom: bool = False
    show_relbar_top: bool = False
    show_relbars: bool = False

    favicons: Favicons = Favicons()

    # Not in Sphinx/Alabaster
    css_files: Tuple[str, ...] = (
        '_static/themabaster.css',
        '_static/pygments.css',
    )
    js_files: Tuple[str, ...] = tuple()
