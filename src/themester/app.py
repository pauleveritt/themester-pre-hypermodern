"""

Systems (e.g. Sphinx) connect to Themester by making a ``ThemesterApp``
which they then store in some well-known, system-specific location.
The ``ThemesterApp`` has all the contracts a system needs to fulfill.

"""

from dataclasses import dataclass, field, InitVar
from typing import Optional, Any, Union

from venusian import Scanner
from viewdom_wired import render
from wired import ServiceRegistry, ServiceContainer

from themester import url
from themester.protocols import Root, View, Resource
from .sphinx import SphinxConfig
from .sphinx.config import HTMLConfig
from .themabaster.config import ThemabasterConfig


@dataclass
class ThemesterApp:
    root: InitVar[Root]
    sphinx_config: InitVar[Optional[SphinxConfig]]
    html_config: InitVar[Optional[HTMLConfig]]
    theme_config: InitVar[Optional[ThemabasterConfig]]
    registry: ServiceRegistry = field(default_factory=ServiceRegistry)
    scanner: Scanner = field(init=False)
    container: ServiceContainer = field(init=False)

    def __post_init__(self, root, sphinx_config=None, html_config=None, theme_config=None):
        # Make a site-wide container versus the per-render container. This
        # container uses the root as its context.
        self.container = self.registry.create_container(context=root)

        # Put some site-wide singletons into the registry, so you
        # can get them there instead of always needing this app instance
        scanner = Scanner(registry=self.registry)

        self.registry.register_singleton(self, ThemesterApp)
        self.registry.register_singleton(root, Root)
        self.registry.register_singleton(scanner, Scanner)
        if sphinx_config:
            self.registry.register_singleton(sphinx_config, SphinxConfig)
        if html_config:
            self.registry.register_singleton(html_config, HTMLConfig)
        if theme_config:
            self.registry.register_singleton(theme_config, ThemabasterConfig)
        scanner.scan(url)

    def scan(self, module):
        """ Get the scanner and scan a module """

        scanner: Scanner = self.container.get(Scanner)
        scanner.scan(module)

    def setup_plugin(self, module):
        """ Call a plugin's setup function """

        scanner = self.container.get(Scanner)
        s = getattr(module, 'wired_setup')
        s(scanner)

    def render(self,
               container: Optional[ServiceContainer] = None,
               context: Optional[Union[Resource, Any]] = None,
               view_name: Optional[str] = None,
               ) -> str:
        """ Render a vdom via a view from a container """

        # If a container was passed in, use it as the basis for a render
        # container. Otherwise, use the site container and bind to it.
        this_container = container if container is not None else self.container
        tc = this_container.get(ThemabasterConfig)

        # If we were passed in a context, make a container with it,
        # bound to the site container. Otherwise, use the site container.
        if context is not None:
            this_container = this_container.bind(context=context)

        # Sometimes we want to use named views
        if view_name:
            this_view = this_container.get(View, name=view_name)
        else:
            this_view = this_container.get(View)

        # Now render a vdom
        this_vdom = this_view()
        return render(this_vdom, container=this_container)
