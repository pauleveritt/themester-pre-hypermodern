"""

Systems (e.g. Sphinx) connect to Themester by making a ``ThemesterApp``
which they then store in some well-known, system-specific location.
The ``ThemesterApp`` has all the contracts a system needs to fulfill.

"""

from dataclasses import dataclass, field
from importlib import import_module
from pathlib import Path
from typing import Optional, Any, Union, Tuple

from venusian import Scanner
from viewdom_wired import render
from wired import ServiceRegistry, ServiceContainer

from themester import url
from themester.config import ThemesterConfig
from themester.protocols import Root, View, Resource


@dataclass
class ThemesterApp:
    themester_config: Optional[ThemesterConfig] = None
    registry: ServiceRegistry = field(default_factory=ServiceRegistry)
    scanner: Scanner = field(init=False)

    def __post_init__(self):
        # Put some site-wide singletons into the registry, so you
        # can get them there instead of always needing this app instance
        self.scanner = Scanner(registry=self.registry)

        self.registry.register_singleton(self, ThemesterApp)
        self.registry.register_singleton(self.scanner, Scanner)
        if self.themester_config:
            self.registry.register_singleton(self.themester_config, ThemesterConfig)
        self.registry.register_singleton(self.themester_config.root, Root)
        self.scanner.scan(url)

    def setup_plugins(self):
        # Stop doing this as part of __post_init__ to let the
        # system have a chance to register things before handing to
        # plugins.

        # Now setup any configured Themester plugins
        for plugin_string in self.themester_config.plugins:
            plugin_module = import_module(plugin_string)
            self.setup_plugin(plugin_module)

    def setup_plugin(self, module):
        """ Call a plugin's setup function """

        s = getattr(module, 'wired_setup')
        s(self.registry, self.scanner)

    def get_static_resources(self) -> Tuple[Path, ...]:
        """ Any plugin that has static resources, return them """

        # TODO This is dumb, to always re-import the plugins just to check
        #   for static resources. Lots of alternatives. Perhaps if
        #   "subscriptions" returns to wired (or here), we can let each
        #   plugin be discovered and introspected. We can't really put
        #   the plugins on the ThemesterApp instance as it might be
        #   getting pickled in Sphinx.

        container = self.registry.create_container()
        tc: ThemesterConfig = container.get(ThemesterConfig)
        plugins = [import_module(plugin_string) for plugin_string in tc.plugins]
        static_resources = []
        for plugin in plugins:
            get_static_resources = getattr(plugin, 'get_static_resources')
            if get_static_resources:
                static_resources += get_static_resources()
        return tuple(static_resources)

    def render(self,
               container: Optional[ServiceContainer] = None,
               context: Optional[Union[Resource, Any]] = None,
               view_name: Optional[str] = None,
               ) -> str:
        """ Render a vdom via a view from a container """

        # If a container was passed in, use it as the basis for a render
        # container. Otherwise, use the site container and bind to it.
        if container:
            this_container = container
        else:
            this_container = self.registry.create_container(context=context)

        # If we were passed in a context, make a container with it,
        # bound to the site container. Otherwise, use the site container.
        # if context is not None:
        #     this_container = this_container.bind(context=context)

        # Sometimes we want to use named views
        if view_name:
            this_view = this_container.get(View, name=view_name)
        else:
            this_view = this_container.get(View)

        # Now render a vdom
        this_vdom = this_view()
        return render(this_vdom, container=this_container)
