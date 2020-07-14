from typing import Protocol, Tuple, Mapping, Union

# TODO Add support for extra attrs
PropsFile = Union[str, Tuple[str, Mapping]]
PropsFiles = Tuple[PropsFile, ...]


class Hasdoc(Protocol):
    """ A callable that does what Sphinx's helper does for hasdoc() """

    def __call__(self, target: str) -> bool:
        """ Determine whether that target path, relative to root, exists """
        ...
