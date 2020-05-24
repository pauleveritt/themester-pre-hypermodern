"""
Minimum possible layout.

"""

from dataclasses import dataclass

from viewdom import html
from viewdom.h import H

from themester.views import view
from .components import MyLayout  # noqa

EXPECTED = '<section><h1>My Site</h1><div><div>One Child</div></div></section>'


# start-after

@view()
@dataclass
class HelloLayout:
    name: str = 'Layout'

    def __call__(self) -> H:
        return html('<{MyLayout}><div>One Child</div><//>')

# result = '<section><h1>My Site</h1><div><div>One Child</div></div></section>'
