from dataclasses import dataclass

from sphinx.application import Sphinx
from sphinx.jinja2glue import BuiltinTemplateLoader
from viewdom import html
from viewdom_wired import render
from wired import ServiceRegistry, ServiceContainer
from wired.dataclasses import register_dataclass, injected, Context

from themester import View
from themester.renderer import Renderer, VDOMRenderer
from themester.resources import Resource, Root


@dataclass
class DummyView:
    resource_name: str = injected(Context, attr='name')

    def __call__(self):
        return html('<div>Hello {self.resource_name}</div>')


class ThemesterBridge(BuiltinTemplateLoader):

    def render(self, template, context) -> str:
        # Get the container and the view
        render_container: ServiceContainer = context['render_container']
        view = render_container.get(View)

        # Render a vdom then a string
        vdom = view()
        response = render(vdom, container=render_container)
        return response


def builder_init(app: Sphinx):
    """ Wire up some global stuff after Sphinx startup """

    # Make a registry and store in Sphinx environment
    registry = ServiceRegistry()
    app.wired_registry = registry

    # Resource tree with a root and one document, then put in the
    # registry as a singleton
    root = Root()
    f1 = Resource(name='f1', parent=root)
    root['f1'] = f1
    registry.register_singleton(root, Root)

    # Create a "base" container and stash on the Sphinx app
    app.site_container = registry.create_container()

    # Register a view and renderer
    register_dataclass(registry, DummyView, View, context=Resource)
    register_dataclass(registry, VDOMRenderer, Renderer)


def inject_page(app, pagename, templatename, context, doctree):
    """ Store a resource-bound container in Sphinx context """

    site_container: ServiceContainer = app.site_container
    root: Root = site_container.get(Root)
    resource = root['f1']
    render_container = site_container.bind(context=resource)
    context['render_container'] = render_container


def setup(app: Sphinx):
    app.connect('builder-inited', builder_init)

    # Not using any of the Sphinx HTML builder machinery
    # nor Jinja2
    bridge = 'themester.sphinx.ThemesterBridge'
    app.config.template_bridge = bridge

    app.connect('html-page-context', inject_page)

    return dict(parallel_read_safe=True)
