import pytest
from bs4 import BeautifulSoup

from themester.protocols import Resource
from themester.sphinx import SphinxConfig, HTMLConfig
from themester.sphinx.models import PageContext
from themester.testing.resources import Site


def test_wired_render_root_view(themester_app, this_pagecontext, html_config, sphinx_config, this_resource):
    context = Site()
    render_container = themester_app.registry.create_container(context=context)
    render_container.register_singleton(this_pagecontext, PageContext)
    render_container.register_singleton(sphinx_config, SphinxConfig)
    render_container.register_singleton(html_config, HTMLConfig)
    render_container.register_singleton(this_resource, Resource)
    rendered = themester_app.render(container=render_container)
    this_html = BeautifulSoup(rendered, 'html.parser')
    title = this_html.select_one('title').text
    assert 'D2 - Themester SiteConfig' == title


def test_wired_render_nocontext_view(themester_app, this_pagecontext, html_config, sphinx_config, this_resource):
    # context = Document(name='Some Document', parent=themester_app.root)
    render_container = themester_app.registry.create_container(context=None)
    render_container.register_singleton(this_pagecontext, PageContext)
    render_container.register_singleton(sphinx_config, SphinxConfig)
    render_container.register_singleton(html_config, HTMLConfig)
    render_container.register_singleton(this_resource, Resource)
    rendered = themester_app.render(container=render_container)
    this_html = BeautifulSoup(rendered, 'html.parser')
    title = this_html.select_one('title').text
    assert 'D2 - Themester SiteConfig' == title


def test_wired_render_document_view(themester_app, this_pagecontext, html_config, sphinx_config, this_resource):
    # context = Document(name='Some Document', parent=themester_app.root)
    render_container = themester_app.registry.create_container(context=None)
    render_container.register_singleton(this_pagecontext, PageContext)
    render_container.register_singleton(sphinx_config, SphinxConfig)
    render_container.register_singleton(this_resource, Resource)
    render_container.register_singleton(html_config, HTMLConfig)
    rendered = themester_app.render(container=render_container)
    this_html = BeautifulSoup(rendered, 'html.parser')
    title = this_html.select_one('title').text
    assert 'D2 - Themester SiteConfig' == title
