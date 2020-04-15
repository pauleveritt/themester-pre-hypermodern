from dataclasses import dataclass

from viewdom import html

from themester.views import view


@view(name='somename')
@dataclass
class NamedView:
    name: str = 'Named'

    def __call__(self) -> str:
        return html('<div>Hello {self.name}</div>')
