"""
This will be assigned to ``theme_config`` on ``ThemesterConfig``.
"""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Tuple

from ..protocols import ThemeConfig, ThemeSphinxConfig


@dataclass(frozen=True)
class NullsterSphinxConfig(ThemeSphinxConfig):

    @staticmethod
    def get_static_resources() -> Tuple[Path, ...]:
        """ Return all the files that should get copied to the static output """

        static_dir = Path(__file__).parent.absolute() / 'static'
        static_resources = static_dir.glob('**/*')
        return tuple(static_resources)


@dataclass(frozen=True)
class NullsterConfig(ThemeConfig):
    sphinx: NullsterSphinxConfig = field(default_factory=NullsterSphinxConfig)
