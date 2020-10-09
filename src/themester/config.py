from dataclasses import dataclass
from typing import Optional, Sequence

from themester.protocols import ThemeConfig


@dataclass
class ThemesterConfig:
    theme_config: Optional[ThemeConfig] = None
    plugins: Sequence[str] = tuple()
