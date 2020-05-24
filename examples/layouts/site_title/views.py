"""
Minimum possible layout.

"""

from dataclasses import dataclass

from viewdom import html
from viewdom.h import H

from themester.views import view
from .components import MyLayout  # noqa

EXPECTED = '<div>Hello Site Name</div>'


# start-after

@view()
@dataclass
class SiteTitleLayout:
    name: str = 'Layout'

    def __call__(self) -> H:
        return html('<{MyLayout} site_name="Site Name" />')

# result = '<div>Hello Site Name/div>'
