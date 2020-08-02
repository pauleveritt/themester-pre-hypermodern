from dataclasses import dataclass

from viewdom import html, VDOM
from viewdom_wired import component


@component()
@dataclass
class About:


    def __call__(self) -> VDOM:
        return html('about')
