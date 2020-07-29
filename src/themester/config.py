from dataclasses import dataclass
from typing import Optional

from themester.testing.resources import Site


@dataclass
class ThemesterConfig:
    root: Optional[Site] = None
