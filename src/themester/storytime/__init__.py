"""
Organize development into component stories.

Component development usually means several activities: testing,
documentation, and visual review in a browser.
"""

from dataclasses import InitVar, field, dataclass, asdict
from importlib import import_module
from inspect import getmodule
from typing import TypeVar, Optional, Dict, Any, Tuple, Type

from bs4 import BeautifulSoup
from venusian import Scanner
from viewdom import VDOM
from viewdom_wired import render, Component

from themester.app import ThemesterApp
from themester.protocols import Resource

C = TypeVar('C')  # Component
S = TypeVar('S')  # Singletons
S1 = TypeVar('S1')  # Singletons

Singletons = Tuple[Tuple[Any, Any], ...]


def get_story_defaults(component: Component) -> Dict:
    """ Given a component, walk ancestors getting story data """

    component_package: str = getmodule(component).__package__
    segments = component_package.split('.')

    # Here's we'll collect some well-known values to use as
    # story defaults
    defaults = dict()
    default_targets = ('resource', 'themester_app', 'component')

    # Work backwards looking for (a) subpackages with stories.py
    # and (b) stories.py with well-known globals such as resource
    counter = 0
    while counter < len(segments):
        if counter == 0:
            # First pass through, don't slice from the end
            this_segment = '.'.join(segments)
        else:
            # Now we're hopping up
            this_segment = '.'.join(segments[:-counter])
        counter += 1

        # Try to import a stories.py from this location
        try:
            stories = import_module(this_segment + '.stories')
        except ModuleNotFoundError:
            continue

        # Now save some defaults: (a) if they aren't already in
        # the dict (because children override parents) and
        # (b) if they are present
        for target in default_targets:
            if target not in defaults:
                try:
                    t = getattr(stories, target)
                    defaults[target] = t
                except AttributeError:
                    pass

    return defaults


@dataclass
class Story:
    component: C
    resource: Optional[Resource] = None
    themester_app: Optional[ThemesterApp] = None
    other_packages: Optional[Tuple] = tuple()
    usage: Optional[VDOM] = None
    props: InitVar[Optional] = None
    extra_props: InitVar[Optional[Dict]] = None
    combined_props: Dict[str, Any] = field(init=False, default_factory=dict)
    singletons: InitVar[Singletons] = tuple()

    def __post_init__(self, props, extra_props, singletons):
        # Set some defaults if they weren't provided
        story_defaults = get_story_defaults(self.component)
        if self.resource is None:
            self.resource = story_defaults['resource']
        if self.themester_app is None:
            self.themester_app = story_defaults['themester_app']

        self.themester_app.setup_plugins()

        # Scan this component package but also any dependent components
        self.themester_app.scanner = Scanner(registry=self.themester_app.registry)
        package = getmodule(self.component)
        self.themester_app.scanner.scan(package)
        [self.themester_app.scanner.scan(pkg) for pkg in self.other_packages]

        # Register any story-specific singletons and/or factories
        for service, iface in singletons:
            self.themester_app.registry.register_singleton(service, iface)

        # Props: dataclass or dict?
        if hasattr(props, '__annotations__'):
            # props is a dataclass so asdict to turn into dictionary
            self.combined_props = asdict(props)
        elif props is not None:
            self.combined_props: Dict[str, Any] = props
        if extra_props:
            self.combined_props = {**self.combined_props, **extra_props}

    @property
    def instance(self) -> C:
        return self.component(**self.combined_props)

    @property
    def vdom(self) -> VDOM:
        return self.instance()

    @property
    def html(self) -> BeautifulSoup:
        container = self.themester_app.registry.create_container()
        container.register_singleton(self.resource, Resource)

        if self.usage is not None:
            rendered = render(self.usage, container=container)
        else:
            rendered = render(self.vdom, container=container)
        this_html = BeautifulSoup(rendered, 'html.parser')
        return this_html
