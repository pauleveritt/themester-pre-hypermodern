#
from dataclasses import dataclass

from viewdom import html

from themester.views import view


@view()
@dataclass
class DefaultView:
    name: str = 'DefaultView'

    def __call__(self) -> str:
        return html('<div>Hello {self.name}</div>')
