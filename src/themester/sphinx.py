from dataclasses import dataclass
from typing import Optional, Dict

from sphinx.application import Sphinx
from sphinx.jinja2glue import BuiltinTemplateLoader
from venusian import Scanner
from viewdom_wired import render
from wired import ServiceRegistry, ServiceContainer
from wired.dataclasses import register_dataclass

from themester import View
from themester.renderer import Renderer, VDOMRenderer
from themester.resources import Root


@dataclass(frozen=True)
class PageContext:
    """ Gather up info from Sphinx HTML page context """

    pagename: str
    body: str
    prev: Optional[Dict[str, str]]
    next: Optional[Dict[str, str]]


class ThemesterBridge(BuiltinTemplateLoader):

    def render(self, template, context) -> str:
        # Get the container and the view
        render_container: ServiceContainer = context['render_container']
        view = render_container.get(View)

        # Render a vdom then return a string
        vdom = view()
        response = render(vdom, container=render_container)
        return response


def builder_init(app: Sphinx):
    """ Wire up some global stuff after Sphinx startup """

    # Make a registry with a Scanner and store in Sphinx environment
    registry = ServiceRegistry()
    scanner = Scanner(registry=registry)
    registry.register_singleton(scanner, Scanner)
    app.wired_registry = registry

    # Create a "base" container and stash on the Sphinx app
    app.site_container = registry.create_container()

    # Go through the configuration and register stuff
    themester_plugins = app.config['themester_plugins']
    for plugin in themester_plugins:
        try:
            plugin.wired_setup(registry)
        except AttributeError:
            # No wired_setup so scan it insted
            scanner.scan(plugin)

    register_dataclass(registry, VDOMRenderer, Renderer)


def inject_page(app, pagename, templatename, context, doctree):
    """ Store a resource-bound container in Sphinx context """

    site_container: ServiceContainer = app.site_container
    root: Root = site_container.get(Root)
    resource = root[pagename]
    render_container = site_container.bind(context=resource)
    context['render_container'] = render_container

    prev = context.get('prev')
    next = context.get('next')
    body = context.get('body', '')

    # Gather the Sphinx per-page render info into an object that
    # can be retrieved from the container
    page_context = PageContext(
        pagename=pagename,
        body=body,
        prev=prev,
        next=next
    )
    render_container.register_singleton(page_context, PageContext)


def setup(app: Sphinx):
    app.add_config_value('themester_plugins', {}, 'env')
    app.connect('builder-inited', builder_init)
    app.config.template_bridge = 'themester.sphinx.ThemesterBridge'
    app.connect('html-page-context', inject_page)

    return dict(parallel_read_safe=True)
