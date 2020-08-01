"""
Set up the container during each resource rendering.

As Sphinx renders a resource, it has a lot of magic stashed into the
"context". Extract that information and "adapt" it for Themester.

"""
from typing import Dict, Any

from markupsafe import Markup
from wired import ServiceContainer

from themester.app import ThemesterApp
from themester.protocols import Root
from themester.sphinx.models import PageContext, Link, Rellink


def make_render_container(
        themester_app: ThemesterApp,
        pagename: str,
):
    """ Make a bound container for processing current page """

    render_container = themester_app.registry.create_container(
        context=themester_app.root
    )
    return render_container


def make_page_context(
        render_container: ServiceContainer,
        context: Dict[str, Any],
        pagename: str,
        toc_num_entries: Dict[str, int],
        sphinxenv_metadata: Dict[str, Dict[str, Any]],
):
    """ Given some Sphinx context information, register a singleton """

    parents = tuple([
        Link(title=link.title, link=link.title)
        for link in context.get('parents')
    ])
    rellinks = tuple([
        Rellink(
            pagename=link[0],
            link_text=link[3],
            title=link[1],
            accesskey=link[2],
        )
        for link in context.get('rellinks')
    ])
    # TODO Make this into a service
    display_toc = toc_num_entries[pagename] > 1 if 'pagename' in toc_num_entries else False
    ccf = context.get('css_files')
    jcf = context.get('css_files')
    css_files = tuple(ccf) if ccf else tuple()
    js_files = tuple(jcf) if jcf else tuple()
    page_context = PageContext(
        body=Markup(context.get('body', '')),
        css_files=css_files,
        display_toc=display_toc,
        hasdoc=context.get('hasdoc'),
        js_files=js_files,
        meta=sphinxenv_metadata,
        metatags=context.get('metatags'),
        next=context.get('next'),
        page_source_suffix=context.get('page_source_suffix'),
        pagename=pagename,
        pathto=context.get('pathto'),
        prev=context.get('prev'),
        sourcename=context.get('sourcename'),
        rellinks=rellinks,
        title=context.get('title'),
        toc=Markup(context.get('toc')),
        toctree=context.get('toctree'),
    )
    render_container.register_singleton(page_context, PageContext)
