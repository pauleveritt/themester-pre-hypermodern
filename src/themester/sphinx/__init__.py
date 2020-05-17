from sphinx.application import Sphinx
from venusian import Scanner
from wired import ServiceRegistry, ServiceContainer
from wired.dataclasses import register_dataclass

from themester.sphinx import views
from themester.sphinx.models import PageContext


def builder_init(app: Sphinx):
    """ Wire up some global stuff after Sphinx startup """

    # Make a registry with a Scanner and store in Sphinx environment
    registry = ServiceRegistry()
    scanner = Scanner(registry=registry)
    registry.register_singleton(scanner, Scanner)
    app.wired_registry = registry

    # Register any default, Themester views, etc.
    views.wired_setup(registry)

    # Go through the configuration and register stuff
    themester_plugins = app.config['themester_plugins']
    for plugin in themester_plugins:
        try:
            plugin.wired_setup(registry)
        except AttributeError:
            # No wired_setup so scan it instead
            scanner.scan(plugin)

    # Create a "base" container and stash on the Sphinx app
    app.site_container = registry.create_container()

    register_dataclass(registry, VDOMRenderer, Renderer)


def inject_page(app, pagename, templatename, context, doctree):
    """ Store a resource-bound container in Sphinx context """

    # If this is a Sphinx site that wants to do resource-oriented
    # pages, get the root then the resource.
    site_container: ServiceContainer = app.site_container
    root: Root = site_container.get(Root, default=None)
    if root:
        resource = root[pagename]
    else:
        resource = None
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
    app.add_config_value('themester_plugins', [], 'env')
    app.connect('builder-inited', builder_init)
    app.config.template_bridge = 'themester.sphinx.template_bridge.ThemesterBridge'
    app.connect('html-page-context', inject_page)

    return dict(parallel_read_safe=True)
