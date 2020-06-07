from typing import Protocol, Optional

from viewdom_wired import Component


class Title(Component, Protocol):
    page_title: str
    site_name: Optional[str]
