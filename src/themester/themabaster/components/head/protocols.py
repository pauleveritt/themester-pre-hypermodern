from typing import Protocol

from viewdom import Children


class Head(Protocol):
    """ A container for the head element and its children """
    children: Children
