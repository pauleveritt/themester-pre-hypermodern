from dataclasses import dataclass
from typing import Optional, Mapping, Iterable


@dataclass(frozen=True)
class DefaultPageContext:
    """ Per-page info from the underlying system needed for by layout """

    body: str
    css_files: Iterable[str]
    js_files: Iterable[str]
    page_title: str
    prev: Optional[Mapping[str, str]] = None
    next: Optional[Mapping[str, str]] = None
