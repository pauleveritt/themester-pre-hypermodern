"""
Content is a block in the Body component.
"""

from dataclasses import dataclass

from viewdom import html, VDOM
from viewdom_wired import component

from .document import Document  # noqa: F401
from .sidebar1 import Sidebar1  # noqa: F401
from .sidebar2 import Sidebar2  # noqa: F401

@component()
@dataclass(frozen=True)
class Content:
    def __call__(self) -> VDOM:
        return html('''\n
<{Sidebar1} />
<div class="document">
    <{Document} />
    <{Sidebar2} />
    <div class="clearer"></div>
</div>
''')
