from typing import Protocol, Iterable

from viewdom.h import H


class Layout(Protocol):
    site_name: str
    children: Iterable[H]
