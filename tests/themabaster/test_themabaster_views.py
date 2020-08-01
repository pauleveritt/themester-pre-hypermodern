from bs4 import BeautifulSoup

from themester.protocols import Root
from themester.sphinx.models import PageContext
from themester.testing.resources import Document


def test_wired_render_root_view(themester_app, this_pagecontext):
    context = Root()
    render_container = themester_app.registry.create_container(context=context)
    render_container.register_singleton(this_pagecontext, PageContext)
    rendered = themester_app.render(container=render_container)
    this_html = BeautifulSoup(rendered, 'html.parser')
    title = this_html.select_one('title').text
    assert 'Some Page - Themester SiteConfig' == title


def test_wired_render_nocontext_view(themester_app, this_pagecontext):
    context = Document(name='Some Document', parent=themester_app.root)
    render_container = themester_app.registry.create_container(context=None)
    render_container.register_singleton(this_pagecontext, PageContext)
    rendered = themester_app.render(container=render_container)
    this_html = BeautifulSoup(rendered, 'html.parser')
    title = this_html.select_one('title').text
    assert 'Some Page - Themester SiteConfig' == title


def test_wired_render_document_view(themester_app, this_pagecontext):
    context = Document(name='Some Document', parent=themester_app.root)
    render_container = themester_app.registry.create_container(context=None)
    render_container.register_singleton(this_pagecontext, PageContext)
    rendered = themester_app.render(container=render_container)
    this_html = BeautifulSoup(rendered, 'html.parser')
    title = this_html.select_one('title').text
    assert 'Some Page - Themester SiteConfig' == title
