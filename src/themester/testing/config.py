from dataclasses import dataclass

from themester import Config


@dataclass
class ThemesterConfig(Config):
    use_resources: bool = False
