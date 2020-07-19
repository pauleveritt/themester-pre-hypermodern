"""
Default implementation of the Themabaster <Body> component.
"""

from dataclasses import dataclass

from viewdom import html, VDOM
from viewdom_wired import component

from .header import Header  # noqa: F401


@component()
@dataclass(frozen=True)
class Body:
    def __call__(self) -> VDOM:
        return html('''\n
<body>
<{Header} />
</body>
''')
