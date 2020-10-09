from dataclasses import dataclass

from viewdom import VDOM, html
from viewdom_wired import component
from wired_injector.operators import Get

from themester.protocols import Resource

try:
    from typing import Annotated
except ImportError:
    from typing_extensions import Annotated


@component()
@dataclass(frozen=True)
class HelloWorld:
    name: str
    title: Annotated[str, Get(Resource, attr='title')]

    def __call__(self) -> VDOM:
        return html('<h1>Site: {self.title}</h1><span>Hello {self.name}</span>')
