"""
This will be assigned to ``theme_config`` on ``ThemesterConfig``.
"""

from dataclasses import dataclass
from pathlib import Path
from typing import Tuple

from ..protocols import ThemeConfig


@dataclass(frozen=True)
class NullsterConfig(ThemeConfig):

    @staticmethod
    def get_static_resources() -> Tuple[Path, ...]:
        """ Return all the files that should get copied to the static output """

        static_dir = Path(__file__).parent.absolute() / 'static'
        static_resources = static_dir.glob('**/*')
        return tuple(static_resources)
