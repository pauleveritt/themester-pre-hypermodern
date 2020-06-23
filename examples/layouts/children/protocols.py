from typing import Protocol, Iterable

from viewdom import VDOM


class Layout(Protocol):
    site_name: str
    children: Iterable[VDOM]
