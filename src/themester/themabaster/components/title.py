from dataclasses import dataclass
from typing import Optional

from markupsafe import Markup
from viewdom import html, VDOM
from viewdom_wired import component


@component()
@dataclass(frozen=True)
class Title:
    page_title: str
    project: Optional[str] = ''

    def __call__(self) -> VDOM:
        if self.project:
            raw_title = f'{self.page_title} - {self.project}'
        else:
            raw_title = f'{self.page_title}'
        title = Markup(raw_title).striptags()
        return html('<title>{title}</title>')
