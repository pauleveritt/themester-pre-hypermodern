"""

Markers for a registry-driven, replaceable config system.

In Themester itself, themester.config is just a protocol that
provides something that can be registered, looked up, and claim
that it is a mapping.

"""

from .protocols import Config

__all__ = [
    'Config'
]
