from typing import Protocol, Optional, Tuple

from viewdom_wired import Component


class JSFiles(Component, Protocol):
    site_files = Tuple[str, ...]
    page_files = Optional[Tuple[str, ...]]
