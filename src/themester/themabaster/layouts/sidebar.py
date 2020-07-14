"""
A layout that has sidebars.
"""
from viewdom import html, VDOM

from ..components.html import HTML  # noqa: F401


def SidebarLayout() -> VDOM:
    return html('''\n
<html>
  <{HTML}>x<//>
</html>
    ''')
