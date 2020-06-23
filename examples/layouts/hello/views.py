from dataclasses import dataclass

from viewdom import html, VDOM

from themester.views import view
from .components import MyLayout  # noqa

EXPECTED = '<div>Hello My Site</div>'


# start-after

@view()
@dataclass
class HelloLayout:
    name: str = 'Layout'

    def __call__(self) -> VDOM:
        return html('<{MyLayout} />')

# result = '<div>Hello My Site/div>'
