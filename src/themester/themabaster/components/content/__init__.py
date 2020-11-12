"""
Content is a block in the Body component.
"""

from dataclasses import dataclass

from viewdom import html, VDOM
from viewdom_wired import component

from ..document import Document
from ...sidebars.sidebar1 import Sidebar1
from ...sidebars.sidebar2 import Sidebar2


@component()
@dataclass(frozen=True)
class Content:
    def __call__(self) -> VDOM:
        assert (Document, Sidebar1, Sidebar2)
        return html('''\n
<{Sidebar1} />
<div class="document">
    <{Document} />
    <{Sidebar2} />
    <div class="clearer"></div>
</div>
''')
