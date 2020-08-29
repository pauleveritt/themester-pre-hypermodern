from dataclasses import dataclass
from typing import Optional, Sequence

from themester.testing.resources import Site


@dataclass
class ThemesterConfig:
    root: Optional[Site] = None
    plugins: Sequence[str] = tuple()
