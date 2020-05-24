from typing import Protocol


class LayoutConfig(Protocol):
    """ Configuration options used in this layout """
    site_name: str


class Layout(Protocol):
    """ All the contracts for any theme implementing this layout """
    site_name: str
