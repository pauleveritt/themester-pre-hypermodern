from typing import Protocol, Optional


class Config(Protocol):
    site_name: Optional[str] = None

