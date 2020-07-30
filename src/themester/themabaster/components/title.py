from dataclasses import dataclass, field
from typing import Optional

from markupsafe import Markup
from viewdom import html, VDOM
from viewdom_wired import component


@component()
@dataclass
class Title:
    page_title: str
    project: Optional[str] = ''
    resolved_title: str = field(init=False)

    def __post_init__(self):
        if self.project:
            raw_title = f'{self.page_title} - {self.project}'
        else:
            raw_title = f'{self.page_title}'
        self.resolved_title = Markup(raw_title).striptags()

    def __call__(self) -> VDOM:
        return html('<title>{self.resolved_title}</title>')
