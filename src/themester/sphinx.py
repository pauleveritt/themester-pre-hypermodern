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
    # resource: Resource = injected(Context)
    container: ServiceContainer

    def __call__(self):
        name = self.container.context.name
        return html('<div>Hello {name}</div>')


class ThemesterBridge(BuiltinTemplateLoader):

    def render(self, template, context):
        container: ServiceContainer = context['container']
        view = container.get(View)
        vdom = view()
        response = render(vdom, container=container)
        return response


def builder_init(app: Sphinx):
    """ Wire up some global stuff after Sphinx startup """

    # Make a registry and store in Sphinx environment
    registry = ServiceRegistry()
    app.wired_registry = registry

    # Resource tree with a root and one document
    root = Root()
    f1 = Resource(name='f1', parent=root)
    root['f1'] = f1
    registry.register_singleton(root, Root)
    app.wired_root = root

    # Register a view and renderer
    register_dataclass(registry, DummyView, View, context=Resource)
    register_dataclass(registry, VDOMRenderer, Renderer)


def inject_page(app, pagename, templatename, context, doctree):
    """ Store a resource-bound container in Sphinx context """

    registry: ServiceRegistry = app.wired_registry
    root: Root = app.wired_root
    resource = root['f1']
    container = registry.create_container(context=resource)
    context['container'] = container


def setup(app: Sphinx):
    app.connect('builder-inited', builder_init)

    # Not using any of the Sphinx HTML builder machinery
    # nor Jinja2
    bridge = 'themester.sphinx.ThemesterBridge'
    app.config.template_bridge = bridge

    app.connect('html-page-context', inject_page)

    return dict(parallel_read_safe=True)
