"""
Sidebar to show a searchbox.
"""

from dataclasses import dataclass
from typing import Callable

from viewdom import VDOM, html
from viewdom_wired import component
from wired.dataclasses import injected

from themester.sphinx import PageContext
from themester.themabaster.services.layoutconfig import ThemabasterConfig


@component()
@dataclass(frozen=True)
class SearchBox:
    builder: str = injected(PageContext, attr='builder')
    pagename: str = injected(PageContext, attr='pagename')
    pathto: Callable[[str], str] = injected(PageContext, attr='pathto')

    def __call__(self) -> VDOM:

        if self.pagename != 'search' and self.builder != 'singlehtml':
            pt = self.pathto('search')
            return html('''\n
<div id="searchbox" style="display: none" role="search" data-testid="searchbox">
    <h3>{{ _('Quick search') }}</h3>
    <div class="searchformwrapper">
        <form class="search" action="{pt}" method="get">
          <input type="text" name="q" />
          <input type="submit" value="Go" />
          <input type="hidden" name="check_keywords" value="yes" />
          <input type="hidden" name="area" value="default" />
        </form>
    </div>
</div>
<script type="text/javascript">$('#searchbox').show(0);</script>
            ''')
        return html('')
