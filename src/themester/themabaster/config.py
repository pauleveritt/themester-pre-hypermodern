"""

An implementation of the protocol for all the knobs for this layout.

In Sphinx, this would be an instance that was left in the ``conf.py``
file then injected into the site container as a singleton.
"""
from dataclasses import dataclass

from .protocols import LayoutConfig


@dataclass
class ThemabasterConfig(LayoutConfig):
    site_name: str
