from dataclasses import dataclass
from typing import Optional, Sequence

from themester.protocols import ThemeConfig
from themester.testing.resources import Site


@dataclass
class ThemesterConfig:
    theme_config: Optional[ThemeConfig] = None
    root: Optional[Site] = None
    plugins: Sequence[str] = tuple()
