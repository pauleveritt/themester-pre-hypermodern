"""
Code re-used in various places.
"""

from typing import Tuple, Mapping, Union

# TODO Add support for extra attrs
PropsFile = Union[str, Tuple[str, Mapping]]
PropsFiles = Tuple[PropsFile, ...]
