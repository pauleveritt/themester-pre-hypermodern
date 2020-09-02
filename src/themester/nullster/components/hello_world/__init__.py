from dataclasses import dataclass

from viewdom import VDOM, html
from viewdom_wired import component


@component()
@dataclass(frozen=True)
class HelloWorld:
    name: str

    def __call__(self) -> VDOM:
        return html('<span>Hello {self.name}</span>')
