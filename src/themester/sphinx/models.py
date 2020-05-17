from dataclasses import dataclass
from typing import Optional, Dict


@dataclass(frozen=True)
class PageContext:
    """ Gather up info from Sphinx HTML page context """

    pagename: str
    body: str
    prev: Optional[Dict[str, str]]
    next: Optional[Dict[str, str]]
