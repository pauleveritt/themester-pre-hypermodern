from bs4 import BeautifulSoup

from themester.sphinx.models import PageContext
from themester.utils import render_view


def test_render_root_view(themabaster_registry, themester_site_deep, this_pagecontext):
    resource = themester_site_deep
    rendered = render_view(
        themabaster_registry,
        resource=resource,
        singletons=((this_pagecontext, PageContext),)
    )
    this_html = BeautifulSoup(rendered, 'html.parser')
    title = this_html.select_one('title').text
    assert 'Themester Site - Themester SiteConfig' == title


def test_render_document_view(themabaster_registry, themester_site_deep, this_pagecontext):
    resource = themester_site_deep['d1']
    rendered = render_view(
        themabaster_registry,
        resource=resource,
        singletons=((this_pagecontext, PageContext),)
    )
    this_html = BeautifulSoup(rendered, 'html.parser')
    title = this_html.select_one('title').text
    assert 'D1 - Themester SiteConfig' == title
