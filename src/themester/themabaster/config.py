"""

An implementation of the protocol for all the knobs for this layout.

In Sphinx, this would be an instance that was left in the ``conf.py``
file then injected into the site container as a singleton.
"""

from dataclasses import dataclass, field
from typing import Optional, Tuple, Callable


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
    show_powered_by: bool = True
    show_relbar_bottom: bool = False
    show_relbar_top: bool = False
    show_relbars: bool = False
    touch_icon: Optional[str] = None

    # Not in Sphinx/Alabaster
    css_files: Tuple[str, ...] = (
        '_static/themabaster.css',
        '_static/pygments.css',
    )
