"""
Content is a block in the Body component.
"""

from dataclasses import dataclass

from viewdom import html, VDOM
from viewdom_wired import component


@component()
@dataclass(frozen=True)
class Content:
    def __call__(self) -> VDOM:
        return html('''\n
content
''')
