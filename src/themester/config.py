from dataclasses import dataclass
from typing import Optional, Sequence

from themester.protocols import ThemeConfig, Root


@dataclass
class ThemesterConfig:
    root: Root
    theme_config: Optional[ThemeConfig] = None
    plugins: Sequence[str] = tuple()
