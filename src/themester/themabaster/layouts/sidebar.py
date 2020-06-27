"""
A layout that has sidebars.
"""
from viewdom import html, VDOM

from themester.themabaster.protocols import HTML  # noqa


def SidebarLayout() -> VDOM:
    return html('''\n
<html>
  <{HTML}>x<//>
</html>
    ''')
