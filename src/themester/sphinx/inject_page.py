"""
Set up the container during each resource rendering.

As Sphinx renders a resource, it has a lot of magic stashed into the
"context". Extract that information and "adapt" it for Themester.

"""
from typing import Dict, Any

from docutils.nodes import Node
from markupsafe import Markup
from sphinx.environment import BuildEnvironment
from wired import ServiceContainer, ServiceRegistry

from themester.app import ThemesterApp
from themester.protocols import Root, Resource
from themester.sphinx.models import PageContext, Link, Rellink
from themester.testing.resources import Document


def make_resource(
        root: Root,
        env: BuildEnvironment,
        pagename: str,
) -> Resource:
    """ Make a resource for the currently-rendering page """

    document_metadata: Dict[str, Any] = env.metadata[pagename]

    # Get the title from either the YAML, or the RST, if it exists.
    # pagenames such as 'genindex' won't be in titles.
    this_rtype = document_metadata.get('type', 'document')
    this_title = document_metadata.get('title', False)
    if not this_title:
        t: Node = env.titles.get(pagename, False)
        if t:
            this_title = t.astext()
        else:
            this_title = pagename
    resource = root if this_rtype == 'homepage' else Document(name=pagename, parent=root, title=this_title)
    return resource


def make_render_container(
        document_metadata: Dict[str, Any],
        registry: ServiceRegistry,
        pagename: str,
        resource: Resource,
):
    """ Make a bound container for processing current page """

    render_container = registry.create_container(
        context=resource,
    )
    render_container.register_singleton(resource, Resource)

    return render_container


def make_page_context(
        render_container: ServiceContainer,
        context: Dict[str, Any],
        pagename: str,
        toc_num_entries: Dict[str, int],
        document_metadata: Dict[str, Any],
):
    """ Given some Sphinx context information, register a singleton """

    parents = tuple([
        Link(title=link['title'], link=link['link'])
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
        meta=document_metadata,
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


def setup(app, pagename, templatename, context, doctree):
    """ Store a resource-bound container in Sphinx context """

    env: BuildEnvironment = app.env
    themester_app: ThemesterApp = getattr(app, 'themester_app')
    registry: ServiceRegistry = themester_app.registry
    container = registry.create_container()
    root = container.get(Root)

    resource = make_resource(root, env, pagename)

    render_container = make_render_container(
        document_metadata=env.metadata[pagename],
        registry=registry,
        pagename=pagename,
        resource=resource,
    )
    context['render_container'] = render_container
    make_page_context(
        render_container=render_container,
        context=context,
        pagename=pagename,
        toc_num_entries=env.toc_num_entries,
        document_metadata=env.metadata[pagename],
    )
