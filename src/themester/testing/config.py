from dataclasses import dataclass

from themester import Config


@dataclass
class ThemesterConfig(Config):
    site_name: str
    use_resources: bool = False
