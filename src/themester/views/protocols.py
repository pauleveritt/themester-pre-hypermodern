from typing import Protocol

from viewdom.h import H


class View(Protocol):
    def __call__(self) -> H:
        ...
