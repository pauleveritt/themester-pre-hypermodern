"""

Make a dataclass that is used in conf.py to configure Sphinx-based
themester.

"""
from dataclasses import dataclass

from themester import Config


@dataclass
class SphinxConfig(Config):
    pass
