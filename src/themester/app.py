"""

Systems (e.g. Sphinx) connect to Themester by making a ``ThemesterApp``
which they then store in some well-known, system-specific location.
The ``ThemesterApp`` has all the contracts a system needs to fulfill.

"""

from dataclasses import dataclass, field, InitVar
from typing import Optional

from venusian import Scanner
from viewdom_wired import render
from wired import ServiceRegistry, ServiceContainer

from themester import Config, Root, View


@dataclass
class ThemesterApp:
    root: InitVar[Root]
    config: InitVar[Optional[Config]]
    registry: ServiceRegistry = field(default_factory=ServiceRegistry)
    scanner: Scanner = field(init=False)
    container: ServiceContainer = field(init=False)

    def __post_init__(self, root, config=None):
        # Make a site-wide container versus the per-render container. This
        # container uses the root as its context.
        self.container = self.registry.create_container(context=root)

        # Put some site-wide singletons into the registry, so you
        # can get them there instead of always needing this app instance
        scanner = Scanner(registry=self.registry)

        self.registry.register_singleton(root, Root)
        self.registry.register_singleton(scanner, Scanner)
        if config:
            self.registry.register_singleton(config, Config)

    def setup_plugin(self, module):
        """ Call a plugin's setup function """

        scanner = self.container.get(Scanner)
        s = getattr(module, 'wired_setup')
        s(scanner)

    def render(self, container: Optional[ServiceContainer] = None) -> str:
        """ Render a vdom via a view from a container """

        # Make a container using the root if there isn't a
        # passed-in container
        this_container = container if container else self.container
        this_view = this_container.get(View)
        this_vdom = this_view()
        return render(this_vdom, container=this_container)
