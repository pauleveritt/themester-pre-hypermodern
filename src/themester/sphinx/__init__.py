from sphinx.application import Sphinx
from venusian import Scanner
from wired import ServiceRegistry, ServiceContainer
from wired.dataclasses import register_dataclass

from themester import Root
from themester.app import ThemesterApp
from themester.sphinx import views
from themester.sphinx.config import SphinxConfig
from themester.sphinx.models import PageContext
from themester.testing.config import ThemesterConfig
from themester.testing.resources import Site


def builder_init(app: Sphinx):
    """ Wire up some global stuff after Sphinx startup """

    site = Site()
    sphinx_config = app.config  # type: ignore
    themester_config: SphinxConfig = sphinx_config.themester_config  # type: ignore
    themester_app = ThemesterApp(root=site, config=themester_config)
    themester_app.setup_plugin(views)
    scanner = themester_app.container.get(Scanner)
    app.themester_app = themester_app  # type: ignore

    # Go through the configuration and register stuff
    themester_plugins = sphinx_config['themester_plugins']
    for plugin in themester_plugins:
        try:
            themester_app.setup_plugin(plugin)
        except AttributeError:
            # No wired_setup so scan it instead
            scanner.scan(plugin)
    #
    # # Create a "base" container and stash on the Sphinx app
    # app.site_container = registry.create_container()
    #
    # register_dataclass(registry, VDOMRenderer, Renderer)


def inject_page(app, pagename, templatename, context, doctree):
    """ Store a resource-bound container in Sphinx context """

    themester_app: ThemesterApp = app.themester_app
    themester_config: ThemesterConfig = app.config.themester_config
    themester_root = themester_app.container.get(Root)

    # If this is a Sphinx site that wants to do resource-oriented
    # pages, get the current resource.
    if themester_config.use_resources:
        resource = themester_root[pagename]
    else:
        resource = themester_root

    render_container = themester_app.container.bind(context=resource)
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
    app.add_config_value('themester_config', SphinxConfig(), 'env')
    app.add_config_value('themester_plugins', [], 'env')
    app.connect('builder-inited', builder_init)
    app.config.template_bridge = 'themester.sphinx.template_bridge.ThemesterBridge'  # type: ignore
    app.connect('html-page-context', inject_page)

    return dict(parallel_read_safe=True)
